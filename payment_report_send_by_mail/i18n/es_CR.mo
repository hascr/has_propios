��          |      �          �  !     �     �  i   �  g   N  %   �     �     �     �       X   4  >  �  �  �  &   t     �  i   �       %   �      �     �  )   �  ,     X   2                      	                              
       <div style="margin: 0px; padding: 0px;">
    <p style="margin: 0px; padding: 0px; font-size: 13px;">
        
       <p>Estimado/a <strong><t t-out="object.partner_id.name or ''">Azure Interior</t></strong></p>
<p>Le información de la transferencia realizada a su cuenta bancaria de la factura <strong><span style="font-weight:bold;" t-out="(object.ref or '').replace('/','-') or ''">BNK1-2021-05-0002</span></strong> por un monto de <strong><span style="font-weight:bold;" t-out="format_amount(object.amount, object.currency_id) or ''">$ 10.00</span></strong> por parte de <strong><t t-out="object.company_id.name or ''">YourCompany</t>.</strong></p>
<p><span style="color:#b71c1c;"><strong><u>Importante:</u></strong></span> El pago puede verse reflejado en su cuenta bancaria inclusive uno o dos días hábiles después de la fecha indicada si se realizó transferencia SINPE.</p>
<p>Si tiene alguna inquietud puede responder a este correo y estaremos solucionando a la mayor brevedad posible.</p>
<p>Saludos,</p> 
        <t t-if="not is_html_empty(user.signature)">
            <br><br>
            <t t-out="user.signature or ''">--<br>Mitchell Admin</t>
        </t>
    </p>
</div>
 Allow to Send Mail Contact Enviar manualmente al proveedor cuando se presiona en la acción de enviar recibo por correo electrónico If you checkbox then customer will get payment receipt automatically by email on validation of Payment. Pago: Comprobante de pago - Proveedor Payment Receipt Supplier Payments Send receipt by email Supplier Send receipts by email {{ object.company_id.name }} - Confirmación de pago - Factura {{ object.ref or 'n/a' }} Project-Id-Version: Odoo Server 17.0-20240227
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2024-04-19 09:59-0600
Last-Translator: 
Language-Team: 
Language: es_CR
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n != 1);
X-Generator: Poedit 3.4.2
 <div style="margin: 0px; padding: 0px;">
    <p style="margin: 0px; padding: 0px; font-size: 13px;">
        
       <p>Estimado/a <strong><t t-out="object.partner_id.name or ''">Azure Interior</t></strong></p>
<p>Le información de la transferencia realizada a su cuenta bancaria de la factura <strong><span style="font-weight:bold;" t-out="(object.ref or '').replace('/','-') or ''">BNK1-2021-05-0002</span></strong> por un monto de <strong><span style="font-weight:bold;" t-out="format_amount(object.amount, object.currency_id) or ''">$ 10.00</span></strong> por parte de <strong><t t-out="object.company_id.name or ''">YourCompany</t>.</strong></p>
<p><span style="color:#b71c1c;"><strong><u>Importante:</u></strong></span> El pago puede verse reflejado en su cuenta bancaria inclusive uno o dos días hábiles después de la fecha indicada si se realizó transferencia SINPE.</p>
<p>Si tiene alguna inquietud puede responder a este correo y estaremos solucionando a la mayor brevedad posible.</p>
<p>Saludos,</p> 
        <t t-if="not is_html_empty(user.signature)">
            <br><br>
            <t t-out="user.signature or ''">--<br>Mitchell Admin</t>
        </t>
    </p>
</div>
 Enviar comprobante de pago a proveedor Contacto Enviar manualmente al proveedor cuando se presiona en la acción de enviar recibo por correo electrónico Si marca la casilla, el proveedor recibirá el comprobante de pago automáticamente por correo electrónico al validar el pago. Pago: Comprobante de pago - Proveedor Comprobante de pago de proveedor Pagos Enviar comprobante por correo a proveedor Enviar comprobantes por correo a proveedores {{ object.company_id.name }} - Confirmación de pago - Factura {{ object.ref or 'n/a' }} 