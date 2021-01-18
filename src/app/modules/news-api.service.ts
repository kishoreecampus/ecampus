import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { map } from "rxjs/operators";

@Injectable({
  providedIn: 'root'
})
export class NewsApiService {
  api_key = 'vE5x2p7M.t9zwhQA8RAVEa0ocNbq8vtkgv7KGuBwKq5UES2gIR0Of9c0c5xIQYLCvw0C99xQS';

  constructor(private http: HttpClient) { }

  login(username: string, password: string) {
    const httpheaders = new HttpHeaders()
      .append('X-API-KEY', this.api_key)
      .append("Access-Control-Allow-Origin", "*")
      .append("Access-Control-Allow-Methods", "DELETE, POST, GET, OPTIONS")
      .append("Access-Control-Allow-Headers", "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With")

    console.log(httpheaders)
    return this.http.post<any>('http://13.232.170.221/authentication/obtain-access-token/', ({ "username": username, "password": password }), { headers: httpheaders })
      .pipe(map(data => {

        return data;
      }));
  }
  getDashboard() {
    let space = ("eCampus " + localStorage.getItem('usertoken'))
    const httpheaders1 = new HttpHeaders().append('Authorization', space)
      .append('X-API-KEY', this.api_key)
      .append("Access-Control-Allow-Origin", "*")
      .append("Access-Control-Allow-Methods", "DELETE, POST, GET, OPTIONS")
      .append('Accept', 'application/json')
    console.log("NewHeaders", httpheaders1)

    return this.http.get('http://13.232.170.221/modules/dashboard/', { headers: httpheaders1 })
  }
}
