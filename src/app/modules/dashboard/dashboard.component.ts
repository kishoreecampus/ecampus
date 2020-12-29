import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {

  constructor(private router: Router) { }

 
  title = 'Card View Demo';
  gridColumns = 3;
  UserName:any="Demo123"
  modules:any=[
  { "id" : 1,"name" : "Pre-Admission", "color" : "Blue"},
  { "id" : 2,"name" : "Student", "color" : "green"},
  { "id" : 3,"name" : "Attendence", "color" : "red"},
  { "id" : 4,"name" : "Fee", "color" : "grees"},
  { "id" : 5,"name" : "Transportation", "color" : "yellow"},
  { "id" : 6,"name" : "Employee", "color" : "grey"},
  { "id" : 7,"name" : "Subject", "color" : "orange"},
  { "id" : 8,"name" : "Exam", "color" : "green"},
  { "id" : 9,"name" : "Media", "color" : "maroon"},
  { "id" : 10,"name" : "Course-Managment", "color" : "red"},
  { "id" : 11,"name" : "Certificates", "color" : "grey"},
  { "id" : 12,"name" : "Visitors-Managment", "color" : "blue"}];
  textArea ="Some Noticdsfdsfl;dglkle"
  ngOnInit(): void {
    
  }
  masters(){
    this.router.navigateByUrl('masters');
  }
  
  settings(){
    alert("clicked")
    this.router.navigateByUrl('settings');
  }
}
