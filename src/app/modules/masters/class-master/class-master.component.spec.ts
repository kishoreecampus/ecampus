import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClassMasterComponent } from './class-master.component';

describe('ClassMasterComponent', () => {
  let component: ClassMasterComponent;
  let fixture: ComponentFixture<ClassMasterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ClassMasterComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ClassMasterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
