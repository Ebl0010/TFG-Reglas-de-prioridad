import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { MenuInputEjecucionComponent } from './menu-input-ejecucion/menu-input-ejecucion.component';
import { InputManualComponent } from './input-manual/input-manual.component'
import { HomeComponent } from './home/home.component';
import { TablaResultadosComponent } from './tabla-resultados/tabla-resultados.component';
import { HistorialBaseDatosComponent } from './historial-base-datos/historial-base-datos.component';
import { AyudaComponent } from './ayuda/ayuda.component';
import { MenuPrincipalComponent } from './menu-principal/menu-principal.component';

const routes: Routes = [
  { path: '',   redirectTo: '/home', pathMatch: 'full' },
  { path: 'input', component: MenuInputEjecucionComponent },
  { path: 'historial/:id', component: HistorialBaseDatosComponent },
  { path: 'input-manual/:id', component: InputManualComponent },
  { path: 'home', component: HomeComponent },
  { path: 'ayuda', component: AyudaComponent },
  { path: 'tabla-resultados', component: TablaResultadosComponent },
  { path: 'tabla-resultados/:id', component: TablaResultadosComponent },
  { path: 'menu-principal', component: MenuPrincipalComponent }
  //{ path: '', redirectTo: '/dashboard', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }