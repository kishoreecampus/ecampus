import { Component, OnInit } from '@angular/core';
import { Router, RouterStateSnapshot, ActivatedRouteSnapshot, CanActivate } from '@angular/router';
import { NewsApiService } from 'src/app/modules/news-api.service'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  name: string = 'admin'
  pwd: any = 'admin'
  model: any = {};
  result: any;
  isLoginError: boolean = false;

  constructor(private router: Router, private _service: NewsApiService) { }

  ngOnInit(): void { }

  submit() {
    this._service.login(this.name, this.pwd).subscribe({
      next: data => {
        this.result = data;
        console.log(this.result);
        localStorage.setItem('usertoken', this.result.access)
        this.router.navigate(['/dashboard']);
      },
      error: error => {
        this.isLoginError = true;
        alert("Check UserName or Password and Enter again!!!");
        console.log("There was some Error", error);
      }
    })
  }

}
