import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { DefaultComponent } from './default.component';
import { DashboardComponent } from 'src/app/modules/dashboard/dashboard.component';
import { RouterModule } from '@angular/router';
import { PreAdmissionComponent } from 'src/app/modules/pre-admission/pre-admission.component';
import { SharedModule } from 'src/app/shared/shared.module';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatCardModule } from "@angular/material/card";
import { MatToolbarModule } from "@angular/material/toolbar";
import { MatButtonModule } from "@angular/material/button";
import {TextFieldModule} from '@angular/cdk/text-field';
import { MatCarouselModule } from '@ngmodule/material-carousel';
import { MastersComponent } from 'src/app/modules/masters/masters.component';
import { GalleryModule } from 'ng-gallery';
import { LightboxModule } from 'ng-gallery/lightbox';


@NgModule({
  declarations: [
    DefaultComponent,
    DashboardComponent,
    PreAdmissionComponent,
    MastersComponent
   
     
  ],
  imports: [
    CommonModule,
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
    LightboxModule
  ],
  providers: []
})
export class DefaultModule { }
