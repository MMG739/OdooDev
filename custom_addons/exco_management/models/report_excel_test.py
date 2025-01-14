import base64
import io
import xlsxwriter
from odoo import models, fields, api

class ReportExcelTest(models.AbstractModel):
    _name = 'excel.report.generator'
    _description = 'Excel Report Generator'

    def generate_excel_report(self, records, fields_to_export, filename):
        # Create an in-memory output file for the new workbook.
        output = io.BytesIO()

        # Create an Excel workbook and add a worksheet.
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()

        # Write headers.
        for col_num, field in enumerate(fields_to_export):
            worksheet.write(0, col_num, field['string'])

        # Fetch the data to be written to the Excel file.
        row = 1
        for record in records:
            for col_num, field in enumerate(fields_to_export):
                worksheet.write(row, col_num, record[field['name']])
            row += 1

        # Close the workbook.
        workbook.close()

        # Get the value of the BytesIO stream
        output.seek(0)
        file_data = output.read()

        # Create the attachment
        attachment = self.env['ir.attachment'].create({
            'name': filename,
            'type': 'binary',
            'datas': base64.b64encode(file_data),
            'store_fname': filename,
            'mimetype': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        })

        # Download the file
        return {
            'type': 'ir.actions.act_url',
            'url': '/web/content/%s?download=true' % (attachment.id),
            'target': 'new',
        }