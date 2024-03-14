from string import Template

template_invoice = Template("""
SELECT i.id, i.invoice_date, i.invoice_number, i.is_initial, i.lease_id, i.cashflow_id, i.status_id, t.dMonth,t.deleted_at, t.re_sync_status
FROM invoice i LEFT JOIN totalleasecf t ON i.cashflow_id = t.idTotalLeaseCF
WHERE i.lease_id = $id AND i.is_initial = 1 AND i.status_id = 1;
""")

template_tlcf = Template("""
SELECT *
FROM totalleasecf
WHERE idLease = $id and is_initial = 1 and dMonth = $period and re_sync_status = 'Active' and deleted_at is null
""")

template_update = Template("""
UPDATE invoice SET cashflow_id = $new_cashflow_id WHERE id = $invoice_id
""")