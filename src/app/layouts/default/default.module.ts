import { NgModule } from '@angular/core';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { DefaultComponent } from './default.component';
import { DashboardComponent } from 'src/app/modules/dashboard/dashboard.component';
import { RouterModule } from '@angular/router';
import { PreAdmissionComponent } from 'src/app/modules/pre-admission/pre-admission.component';
import { SharedModule } from 'src/app/shared/shared.module';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatCardModule } from "@angular/material/card";
import { MatSelectModule } from '@angular/material/select';
import { MatToolbarModule } from "@angular/material/toolbar";
import { MatButtonModule } from "@angular/material/button";
import {TextFieldModule} from '@angular/cdk/text-field';
import { MatCarouselModule } from '@ngmodule/material-carousel';
import { MastersComponent } from 'src/app/modules/masters/masters.component';
import { ProfileComponent } from  'src/app/modules/masters/profile/profile.component';
import { ClassMasterComponent } from  'src/app/modules/masters/class-master/class-master.component'
import { SettingsComponent } from 'src/app/modules/settings/settings.component';
import { GalleryModule } from 'ng-gallery';
import { LightboxModule } from 'ng-gallery/lightbox';
import { MatFormFieldModule } from '@angular/material/form-field';
import { NgImageSliderModule } from 'ng-image-slider';
import { HttpClientModule } from '@angular/common/http';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatNativeDateModule } from '@angular/material/core';

@NgModule({
  declarations: [
    DefaultComponent,
    DashboardComponent,
    PreAdmissionComponent,
    MastersComponent,
    ProfileComponent,
    ClassMasterComponent,
    SettingsComponent
   
     
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    RouterModule,
    SharedModule,
    FlexLayoutModule,
    MatCardModule,
    MatToolbarModule,
    MatButtonModule,
    TextFieldModule,
    FormsModule,
    MatCarouselModule.forRoot(),
    GalleryModule,
    LightboxModule,
    MatFormFieldModule,
    MatSelectModule,
    HttpClientModule,
    MatDatepickerModule,
    MatNativeDateModule
    
  ],
  exports:[
    NgImageSliderModule
  ],
  providers: []
})
export class DefaultModule { }
