import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InputComponentInputComponent } from './input.component';

describe('InputComponent', () => {
  let component: InputComponentInputComponent;
  let fixture: ComponentFixture<InputComponentInputComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InputComponentInputComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InputComponentInputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
