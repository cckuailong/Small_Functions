package main

import (
	"fmt"
	"github.com/bitly/go-simplejson"
	"io"
	"io/ioutil"
	"net/http"
	"net/url"
	"os"
	"strconv"
	"strings"
	"time"
)

type INFO struct{
	gs_name string
	gs_pwd string
	git_name string
	git_pwd string
	addr string
	delay string
	cookie string
}


func (info *INFO)init(){
	info.gs_name = "gitstar_username"
	info.gs_pwd = "gitstar_pwd"
	info.git_name = "github_username"
	info.git_pwd = "github_pwd"
	info.addr = "218.241.135.34:88"   // git star url
	info.delay = "6"      // request github every  n seconds
	info.cookie = ""
}

// http request func
func (info *INFO)http_req(uri string, value url.Values, method string, headers map[string]string) (*http.Response){
	var pv io.Reader
	if value != nil{
		post_value := value.Encode()
		pv = strings.NewReader(post_value)
	}else{
		pv=nil
	}
	req, err := http.NewRequest(method, uri, pv)
	if err != nil{
		os.Exit(1)
	}
	if headers != nil{
		for k,v := range(headers){
			req.Header.Add(k, v)
		}
	}
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil{
		os.Exit(1)
	}
	return resp
}

// gitStar
// login gitstar website to get your own cookie on it
func (info *INFO)loginGitStar(){
	uri := "http://" + info.addr + "/api/user/login"
	value := url.Values{
		"username":{info.gs_name},
		"password":{info.gs_pwd},
	}
	method := "POST"
	headers := make(map[string]string)
	headers["Content-Type"] = "application/x-www-form-urlencoded"
	resp := info.http_req(uri, value, method, headers)
	tmp := resp.Header.Get("Set-Cookie")
	info.cookie = tmp
}

func (info *INFO)getGitStarList() []string{
	uri := "http://" + info.addr + "/api/users/" + info.gs_name + "/status/"
	value := url.Values{}
	method := "GET"
	res := make([]string,0)
	headers := make(map[string]string)
	headers["Accept"] = "application/json"
	headers["Cookie"] = info.cookie
	resp := info.http_req(uri, value, method, headers)
	body, _ := ioutil.ReadAll(resp.Body)
	list, _ :=  simplejson.NewJson(body)
	items, _ := list.Array()
	for i, _ := range(items){
		res = append(res, list.GetIndex(i).Get("Repo").MustString())
	}
	return res
}

func (info *INFO)update_gs(){
	uri := "http://" + info.addr + "/star_update"
	headers := make(map[string]string)
	headers["Accept"] = "application/json"
	headers["Cookie"] = info.cookie
	for{
		resp := info.http_req(uri, nil, "GET", headers)
		if resp.StatusCode == 200{
			break
		}
	}
}

// github
func (info *INFO)star(repo string){
	uri := "https://api.github.com/user/starred/" + repo
	req, _ := http.NewRequest("PUT", uri, nil)
	req.SetBasicAuth(info.git_name, info.git_pwd)
	req.Header.Add("Content-Length", "0")
	client := &http.Client{}
	client.Do(req)
}


func run_star(){
	test := INFO{}
	test.init()
	test.loginGitStar()
	repos := test.getGitStarList()
	fmt.Printf("%d\n", len(repos))
	for i, repo := range(repos){
		test.star(repo)
		fmt.Printf("%d\n", i)
		tt, _ := strconv.Atoi(test.delay)
		time.Sleep(time.Duration(tt))
	}
	if len(repos) > 0{
		test.update_gs()
	}
}
