import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-card',
  templateUrl: './card.component.html',
  styleUrls: ['./card.component.css']
})
export class CardComponent implements OnInit {
  
  produtos:string[] = [];
  manuType:string = "admin";

  constructor() { 
    this.produtos = [
      "mouse",
      "teclado",
      "monitor",
      "fonte"
    ]
  }

  ngOnInit(): void {
  }

  add(){
    this.produtos.pop();
  }

  remover(index:number){
    this.produtos.splice(index, 1);
  }
}
  