import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DefaultComponent } from './layouts/default/default.component';
import { DashboardComponent } from './modules/dashboard/dashboard.component';
import { MastersComponent } from './modules/masters/masters.component';
import { SettingsComponent } from './modules/settings/settings.component';
import { PreAdmissionComponent } from './modules/pre-admission/pre-admission.component';
import { ProfileComponent } from './modules/masters/profile/profile.component'
import { ClassMasterComponent } from './modules/masters/class-master/class-master.component';
import { LoginComponent } from './modules/login/login.component';
import { AuthGuard } from './auth.guard'

const routes: Routes = [
  {
    path: '',
    component: DefaultComponent,
    children: [{
      path: 'login',
      component: LoginComponent
    },
    {
      path: 'dashboard',
      component: DashboardComponent,
      canActivate: [AuthGuard]
    },
    {
      path: 'preAdmission',
      component: PreAdmissionComponent
    },
    {
      path: 'masters',
      component: MastersComponent
    },
    {
      path: 'settings',
      component: SettingsComponent
    },
    {
      path: 'masters/profile',
      component: ProfileComponent
    },
    {
      path: 'masters/classMaster',
      component: ClassMasterComponent
    }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
