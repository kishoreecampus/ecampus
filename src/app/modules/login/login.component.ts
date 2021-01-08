import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NewsApiService } from 'src/app/modules/news-api.service'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  name:string='admin'
  pwd:any='admin'
  model: any = {};
  result:any;
  
  constructor(private router: Router,private _service : NewsApiService ) { }

  ngOnInit(): void {
  
    
  }
  submit(){
    // if(this.name =='demo' && this.pwd == 'demo123'){
    //   this.router.navigateByUrl('/dashboard');
    // }else{
    //   alert("invalid UserName or Password");
    // }

    this._service.login(this.name,this.pwd).subscribe({
      next:data =>{
        this.result=data;
        console.log(this.result);
      },
      error:error=>{
        console.log("There was some Error",error);
      }
    })
  }
  
}
