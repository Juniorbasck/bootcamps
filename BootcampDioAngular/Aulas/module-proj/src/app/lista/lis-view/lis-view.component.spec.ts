import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LisViewComponent } from './lis-view.component';

describe('LisViewComponent', () => {
  let component: LisViewComponent;
  let fixture: ComponentFixture<LisViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LisViewComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LisViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
