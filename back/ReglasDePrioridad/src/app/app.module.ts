import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
/*import { MenuLateral3Component } from './menu-lateral3/menu-lateral3.component';
import { MenuLateral2Component } from './menu-lateral2/menu-lateral2.component';
import { MenuSuperiorComponent } from './menu-superior/menu-superior.component';*/
import { MenuInputEjecucionComponent } from './menu-input-ejecucion/menu-input-ejecucion.component';
import { AppRoutingModule } from './app-routing.module';
import { HomeComponent } from './home/home.component';
import { InputManualComponent } from './input-manual/input-manual.component';
import { ContactListComponent } from './contact-list/contact-list.component';
import { HttpClientModule } from  '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
   
    MenuInputEjecucionComponent,
    HomeComponent,
    InputManualComponent,
    ContactListComponent
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }