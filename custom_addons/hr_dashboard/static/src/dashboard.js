/** @odoo-module **/
import {  Component, useState, mount } from "@odoo/owl";
import { registry } from "@web/core/registry";


class HrDashboard extends Component {
    static template = "hr_dashboard.HrDashboard";
}


registry.category("actions").add("hr_dashboard.dashboard", HrDashboard);