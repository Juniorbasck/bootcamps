import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { InputComponentInputComponent } from './input/input.component';
import { LisViewComponent } from './lis-view/lis-view.component'



@NgModule({
  declarations:[
    InputComponentInputComponent,
    LisViewComponent
  ],
  exports:[
    InputComponentInputComponent,
    LisViewComponent
  ],
  imports: [
    CommonModule
  ]
})
export class ListaModule { }
