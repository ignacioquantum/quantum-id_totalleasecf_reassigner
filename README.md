# idTotalLeaseCF Reassigner

## Descripcion

Existirán operaciones(Leases) que serán reestructuradas sus tablas de amortizacion(TotalLeaseCF) por medio del PMS, ya que se cambiará su fecha de inicio de pago de rentas. Al ser reestructurada la operacion todos sus idTotalLeaseCF serán reasignados para todas aquellas rentas que no tengan facturas asignadas. 

En especifico, las rentas iniciales de estas operaciones, ya tienen factura y pago/s, por lo que no solo pueden ser reasignadas por medio del PMS, por lo que mediante un script se debe identificar esta factura inicial y reasignar su idTotalLeaseCF al correcto

A su vez, se debe de eliminar el id_Odoo ya que no correspondería a ninguno en produccion ya que ya se tiene pagado y facturado

Todo esto dentro de la tabla Invoice
