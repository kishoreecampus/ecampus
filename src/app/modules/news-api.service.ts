import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders  } from '@angular/common/http';
import { map } from "rxjs/operators"; 

@Injectable({
  providedIn: 'root'
})
export class NewsApiService {
  api_key = 'ZGh9TSKi.N2HtDAQ5LuqKtG4E50dGpGoHeVtVOR5ELTcYx5p9sf4UmH2HG8esCCfpNKprXC0n';
  url='http://13.232.170.221/authentication/obtain-access-token/';
  constructor(private http:HttpClient) { }
  initSources(){
    return this.http.get('https://newsapi.org/v2/sources?language=en&apiKey='+this.api_key);
 }
 initArticles(){
  return this.http.get('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey='+this.api_key);
 }
 getArticlesByID(source: String){
  return this.http.get('https://newsapi.org/v2/top-headlines?sources='+source+'&apiKey='+this.api_key);
 }
 login(username:string,password:string){
   let data={'username':username,'password':password}
  //  let headers = new Headers();
  //  headers.append('Content-Type','application/json');
  //  headers.append('X-API-KEY','ZGh9TSKi.N2HtDAQ5LuqKtG4E50dGpGoHeVtVOR5ELTcYx5p9sf4UmH2HG8esCCfpNKprXC0n')
   
  return this.http.post<any>(this.url,data,{
    headers:new HttpHeaders({
      'Content-Type':'application/json',
      'X-API-KEY':this.api_key
    })
  })
  .pipe(map(res => {
     
      // }
      console.log(res);
      return res;
  }));
 }
}
