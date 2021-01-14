import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NewsApiService } from 'src/app/modules/news-api.service'
import { NgxSpinnerService } from "ngx-spinner";
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(private router: Router, private _service: NewsApiService, private SpinnerService: NgxSpinnerService) { }
  title = 'Card View Demo';
  gridColumns = 3;
  UserName: any = "Demo123"

  modules: any;
  textArea = "Some Noticdsfdsfl;dglkle"
  ngOnInit(): void {
    console.log(sessionStorage);

    this.getDashboardItems();
  }
  masters() {
    this.router.navigateByUrl('masters');
  }

  settings() {
    alert("clicked")
    this.router.navigateByUrl('settings');
  }
  getDashboardItems() {
    this.SpinnerService.show();
    this._service.getDashboard().subscribe((res) => {
      console.log("response reacived");
      this.modules = res
      this.SpinnerService.hide();
      console.log(this.modules)
    },
      (error) => {
        console.error('Request failed with error')
      },
      () => {
        console.error('Request completed')
      })
  }
}
