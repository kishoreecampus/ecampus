import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
date;
  constructor(public route: Router) {setInterval(() => {
    this.date = new Date()
  }, 1000) }

  ngOnInit(): void {
    
  }
  schoolName='GoodWill High School';
  image=".././assets/images/sampleLogo.png"
}
