import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

interface IMongoItem {
  title: string;
  _id: {
    $oid: string
  };
  date_modified: {
    $date: Date
  };
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'angular-app';

  text: string;
  error: string;
  mongoItem: IMongoItem;

  callPy() {
    this.http$.get(environment.endpoint).subscribe(
      res => this.text = JSON.stringify(res)
    );
  }

  callR() {
    return this.http$.get(`${environment.endpoint}/r`).subscribe(
      json => {
        this.text = JSON.stringify(json);
      }
    );
  }

  addDoc() {
    this.http$.post<IMongoItem>(`${environment.endpoint}/api/add`, {}).subscribe(
      json => {
        this.mongoItem = json;
      }
    );
  }

  removeDoc(id: string) {
    this.http$.delete<{'ok': number}>(`${environment.endpoint}/api/remove?id=${id}`).subscribe(
      json => {
        if (json.ok === 1) {
          this.mongoItem = null;
        }
      }
    );
  }

  constructor(private http$: HttpClient) {}
}
