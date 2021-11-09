import { Component,OnInit } from '@angular/core';
import * as parameters from '../app/numericalParameters'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'numericalAnalisis';
  parameters=parameters.parameters;
  selectedOption=0
  isMatrix=false
  selectedMethod: any

  methodSelect(){
    console.log(this.selectedOption)
     this.selectedMethod=this.parameters[this.selectedOption]
    for (var parameter in this.selectedMethod.parameters){
      console.log(parameter)

    }
  }
  

}
