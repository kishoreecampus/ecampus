import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DefaultComponent } from './layouts/default/default.component';
import { DashboardComponent } from './modules/dashboard/dashboard.component';
import { MastersComponent } from './modules/masters/masters.component';
import { PreAdmissionComponent } from './modules/pre-admission/pre-admission.component';


const routes: Routes = [
{path:'',
component:DefaultComponent,
children:[{
  path:'',
  component:DashboardComponent
},
{
  path:'preAdmission',
  component:PreAdmissionComponent
},
{
  path:'masters',
  component:MastersComponent
}
]
} 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
