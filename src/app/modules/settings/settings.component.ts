import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  title = 'Card View Demo';
  gridColumns = 3;
  UserName:any="Demo123"
  constructor(private router: Router) { }

  ngOnInit(): void {
  }
  home(){
    this.router.navigateByUrl('/');
  }
  masters(){
    this.router.navigateByUrl('masters');
  }

}
