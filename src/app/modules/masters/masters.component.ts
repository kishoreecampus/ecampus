import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-masters',
  templateUrl: './masters.component.html',
  styleUrls: ['./masters.component.css']
})
export class MastersComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {

  }
  title = 'Card View Demo';
  gridColumns = 3;
  UserName: any = "Demo123"
  modules: any = [
    { "id": 1, "name": "Profile", "color": "orange" },
    { "id": 2, "name": "Room Management", "color": "violet" },
    { "id": 3, "name": "Class Master", "color": "green" },
    { "id": 4, "name": "Caste Master", "color": "grey" }
  ];
  textArea = "Some Noticdsfdsfl;dglkle"

  home() {
    this.router.navigateByUrl('/dashboard');
  }
  settings() {
    this.router.navigateByUrl('settings');
  }
  profile(id) {
    if (id == 'Profile') {
      this.router.navigateByUrl('/masters/profile');
    }
    else if (id == 'Class Master') {
      this.router.navigateByUrl('/masters/classMaster');
    }
    else {
      alert("Under Process");
    }

  }

}
