import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DateAdapter } from '@angular/material/core';
import { DatePipe } from '@angular/common';
import { FormGroup, FormBuilder, FormArray } from '@angular/forms'
@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  title = 'Card View Demo';
  gridColumns = 3;
  UserName: any = "Demo123"
  textArea = "some Notices";
  picker: any;
  date: any
  unavailability = { startDate: "2020-01-01T22:00:00.000Z", endDate: "2021-11-24T22:00:00.000Z" }
  unavailability1 = { startDate: "2020-01-01T22:00:00.000Z", endDate: "2021-11-24T22:00:00.000Z" }
  unavailabilityForm: FormGroup;
  unavailabilityForm1: FormGroup;
  startDate = new DatePipe('en-US')
  selectedAcadamiceYear = [{ "FromDate": '', "ToDate": '' }];
  selectedFinanceYear = [{ "FromDate": '', "ToDate": '' }];
  constructor(private router: Router, private dateAdapter: DateAdapter<Date>, private formBuilder: FormBuilder) {
    this.dateAdapter.setLocale('en-GB');
    this.unavailabilityForm = this.formBuilder.group({
      startDate: [this.unavailability.startDate],
      endDate: [this.unavailability.endDate]
    });
    this.unavailabilityForm1 = this.formBuilder.group({
      startDate: [this.unavailability1.startDate],
      endDate: [this.unavailability1.endDate]
    });
  }

  ngOnInit(): void {
  }
  home() {
    this.router.navigateByUrl('/dashboard');
  }
  masters() {
    this.router.navigateByUrl('masters');
  }

  createAcadmicYear() {
    // alert(this.startDate);
    const now = Date.now();
    const sample = this.startDate.transform(now, 'short');
    alert(sample);

  }
  createFinanceYear() {

  }

}
