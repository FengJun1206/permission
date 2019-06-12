from app.my_primission import permission_hook

# app 名字_(url_name)
perm_dic = {

    'app_staff_detail': ['staff_detail', 'GET', [], {}],  # 可以查看员工个人信息
    'app_fina_state': ['fina_state', 'GET', [], {}],  # 可以查看财务报表
    'app_payroll': ['payroll', 'GET', [], {}],  # 可以查看工资条

    # 'crm_table_list_view': ['table_obj_change', 'GET', [], {}],  # 可以访问表里每条数据的修改页
    # 'crm_table_list_change': ['table_obj_change', 'POST', [], {}],  # 可以对表里的每条数据进行修改
    # 'crm_table_obj_add_view': ['table_obj_add', 'GET', [], {}],  # 可以访问数据增加页
    # 'crm_table_obj_add': ['table_obj_add', 'POST', [], {}],  # 可以创建表里的数据

}
