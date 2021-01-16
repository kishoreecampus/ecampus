import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { first } from 'rxjs/operators';


@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  textArea = "Some Noticdsfdsfl;dglkle"
  UserName: any = "Demo123"
  registerForm: FormGroup;
  loading = false;
  submitted = false;
  model: any = {}
  constructor(private formBuilder: FormBuilder, private router: Router) { }

  ngOnInit() {
    this.registerForm = this.formBuilder.group({
      trustName: ['', Validators.required],
      instutionName: ['', Validators.required],
      address1: ['', Validators.required],
      address2: ['', Validators.required],
      administrator: ['', Validators.required],
      mobile: ['', Validators.required],
      websiteName: ['', Validators.required],
      phone: ['', [Validators.required, Validators.minLength(12)]]
    });
  }
  register() {
    console.log(this.model)
  }

  home() {
    this.router.navigateByUrl('/dashboard');
  }
  masters() {
    this.router.navigateByUrl('/masters');
  }
}
