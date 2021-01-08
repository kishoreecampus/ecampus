import { Component, OnInit } from '@angular/core';
 import { LoginComponent} from 'src/app/modules/login/login.component'
 import { SidebarComponent } from 'src/app/shared/components/sidebar/sidebar.component'
 import { Router,NavigationEnd  } from '@angular/router';

@Component({
  selector: 'app-default',
  templateUrl: './default.component.html',
  styleUrls: ['./default.component.css'],
  providers:[LoginComponent,SidebarComponent]
})
export class DefaultComponent implements OnInit {
  sideMenu:boolean=false;
  public href: string = "";
  constructor(private loginComponet : LoginComponent,private router: Router) { 
    this.href = this.router.url;
    console.log(this.router.url);
   
    this.router.events.subscribe((ev) => {
      
      if (ev instanceof NavigationEnd) { 
        this.href = this.router.url;
        if(this.href =='' || this.href =='/'){
          this.sideMenu = false;
        }else{
          this.sideMenu =true;
        }
    }
    });
  }
  
  ngOnInit(): void {
   
      
      
    
  }

}
