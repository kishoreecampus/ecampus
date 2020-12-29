import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-class-master',
  templateUrl: './class-master.component.html',
  styleUrls: ['./class-master.component.css']
})
export class ClassMasterComponent implements OnInit {
  classGroup=[{"groupName":''}]
  class=[{"className":''}]
  section=[{"classGroup":'',"className":'',"sectionName":''}]
  textArea="gfdgjkdfgjdfgkjfhjk"
  constructor(private router: Router) { }
  selected = 'option2';
  UserName='Demo123'
  classgroup:any;
  selectedGroupName:any;
  classname:any;
  selectedClassName:any;
  sectionName:any;
  ngOnInit(): void {
  }
  home(){
    this.router.navigateByUrl('/');
  }
  masters(){
    this.router.navigateByUrl('/masters');
  }
  createClassGroup(classgroup: any){
    alert(classgroup);
    this.classGroup.push({"groupName":classgroup})
    console.log(this.class);
  }
  createClass(classname: any){
    alert(classname);
    this.class.push({"className":classname})
  }
  createSection(selectedGroupName: any,selectedClassName: any,sectionName: any){
    alert(sectionName);
    this.section.push({"classGroup":selectedGroupName,"className":selectedClassName,"sectionName":sectionName})
    console.log(this.section);
  }
}
