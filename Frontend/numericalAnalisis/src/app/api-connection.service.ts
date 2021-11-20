import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiConnectionService {

  constructor(private http:HttpClient) { }

  runMethod(apiObj:any){
    //return this.http.post("http://ec2-54-152-129-162.compute-1.amazonaws.com/callMethod",apiObj)
    return this.http.post("http://192.168.1.8:80/callMethod",apiObj)
    
  }
}
