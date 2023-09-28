from kivymd.app import MDApp
import boto3
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from screen_nav import screen_helper
import pymysql
from kivy.properties import BooleanProperty, ListProperty, StringProperty, ObjectProperty
from kivymd.toast import toast
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import AsyncImage
import os
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
Bucket_Name = "mobileappbucket-new"
s3_client = boto3.client('s3', aws_access_key_id="AKIA4WFGH2B7OWNMKKU4", aws_secret_access_key="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")

conn = pymysql.connect(host="appdatabase.czrro6tu6hbs.us-east-2.rds.amazonaws.com", user="admin", password="admin123", db="SnowRemovalApp")
cursor = conn.cursor()

Window.size = (450, 580)

screen_helper = """
#: import get_color_from_hex kivy.utils.get_color_from_hex

ScreenManager:
    id: sm
    TopPage:
        MDFloatLayout:
            md_bg_color: 43/255, 135/255, 168/255, 1
            Image:
                source: "static/myfiles/1.png"
                size_hint: .24,.24
                pos_hint: {"center_x":.5, "center_y":.55}
                canvas.before:
                    Color:
                        rgb: 1,1,1,1
        MDLabel:
            text: "SNOW REMOVAL"
            pos_hint: {"center_x":.7, "center_y":.4}
            haling: "center"
            theme_text_color: "Custom"
            text_color: 1,1,1,1
            font_size: "38sp"
            font_name: "Comic"
        MDRoundFlatButton:
            text: "HOME"
            pos_hint: {"center_x":.5, "center_y":.3}
            font_size: 20
            md_bg_color: 0, 0, 0, 1
            on_press: app.root.current='menu'
    MenuScreen:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    CustomerRegistration:
        id: customerreg
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    ServiceProviderReg:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    AdminHome:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
        MDRoundFlatButton:
            text: "Admin Home"
            pos_hint: {"center_x":.5, "center_y":.3}
            font_size: 20
            md_bg_color: 0, 0, 0, 1
            on_press: app.root.current='adminmenu'
    AdminScreen:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    ViewLocations:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1
    ViewCategory:
        MDTopAppBar:
            pos_hint: {"top": 1}
            title: "Snow Removal App"
            icon_left: "arrow"
            elevation: 8
            md_bg_color: 43/255, 135/255, 168/255, 1


<MenuScreen>
    name: 'menu'
    admin_email : admin_email
    admin_password : admin_password
    MDBottomNavigation:
        md_bg_color: 43/255, 135/255, 168/255, 1
        MDBottomNavigationItem:
            name: "screen1"
            text: "Home"
            color:  1, 0, 0, 0.9
            font_name: "Comic"
            font_size: 20
            MDLabel:
                text: "Welcome to Snow Removal App"
                font_name: "Comic"
                font_size: 40
                halign: "center"
        MDBottomNavigationItem:
            name: "screen2"
            text: "Admin"
            font_name: "Comic"
            font_size: 20
            MDCard:
                size_hint: None,None
                size: 450,550
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 20
                spacing: 30
                orientation: "vertical"
                MDLabel:
                    text: "ADMIN LOGIN"
                    color:  0, 0, 0, 0.9
                    font_name: "Comic"
                    font_style: 'Button'
                    font_size: 40
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: 15
                MDTextField:
                    id: admin_email
                    mode: "round"
                    hint_text: "Email"
                    multiline: False
                    font_name: "Comic"
                    icon_right: "email"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                MDTextField:
                    id : admin_password
                    mode: "round"
                    hint_text: "Password"
                    font_name: "Comic"
                    icon_right: "eye-off"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    password: True
                MDRoundFlatButton:
                    text: "LOGIN"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.admin_login()
                Widget:
                    size_hint_y: None
                    height: 30
        MDBottomNavigationItem:
            name: "screen3"
            text: "Service"
            font_name: "Comic"
            font_size: 20
            MDCard:
                size_hint: None,None
                size: 450,550
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 20
                spacing: 30
                orientation: "vertical"
                MDLabel:
                    text: "SERVICE PROVIDER LOGIN"
                    color:  0, 0, 0, 0.9
                    font_name: "Comic"
                    font_style: 'Button'
                    font_size: 40
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: 15
                MDTextField:
                    hint_text: "Email"
                    font_name: "Comic"
                    icon_right: "account"
                    mode: "round"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    normal_color : [1,1,0,1]
                    on_text: self.text = self.text.replace(" ", "")
                MDTextField:
                    mode: "round"
                    hint_text: "Password"
                    font_name: "Comic"
                    icon_right: "eye-off"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    password: True
                    on_text: self.text = self.text.replace(" ", "")
                MDRoundFlatButton:
                    text: "LOGIN"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                MDRectangleFlatButton:
                    text: "REGISTER HERE"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.manager.current='serviceproviderreg'
                Widget:
                    size_hint_y: None
                    height: 15
        MDBottomNavigationItem:
            name: "screen4"
            text: "Customer"
            font_name: "Comic"
            font_size: 20
            MDCard:
                size_hint: None,None
                size: 450,550
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 20
                spacing: 30
                orientation: "vertical"
                MDLabel:
                    text: "CUSTOMER LOGIN"
                    color:  0, 0, 0, 0.9
                    font_name: "Comic"
                    font_style: 'Button'
                    font_size: 40
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: 15
                MDTextField:
                    id: email
                    hint_text: "Email"
                    font_name: "Comic"
                    icon_right: "account"
                    mode: "round"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    normal_color : [1,1,0,1]
                    on_text: self.text = self.text.replace(" ", "")
                MDTextField:
                    id: password
                    mode: "round"
                    hint_text: "Password"
                    font_name: "Comic"
                    icon_right: "eye-off"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    password: True
                    on_text: self.text = self.text.replace(" ", "")
                MDRoundFlatButton:
                    text: "LOGIN"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_release: app.receive_data(email,password)
                MDRectangleFlatButton:
                    text: "REGISTER HERE"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.manager.current='customerreg'
                Widget:
                    size_hint_y: None
                    height: 15
<AdminHome>
    name: 'adminhome'
    MDLabel:
        text: "Welcome to Admin"
        font_name: "Comic"
        font_size: 40
        halign: "center"
    MDRoundFlatButton:
        text: "BACK"
        pos_hint: {"center_x":.5, "center_y":.2}
        font_size: 20
        md_bg_color: 0, 0, 0, 1
        on_press: app.root.current='menu'

<CustomerRegistration>
    name: 'customerreg'
    fname : fname
    email : email
    phone : phone
    password : password
    address : address
    longitude : longitude
    latitude : latitude
    MDCard:
        size_hint: None,None
        size: 500,550
        pos_hint: {"center_x":.5,"center_y":.5}
        elevation: 5
        md_bg_color: [120, 120, 120]
        padding: 10
        spacing: 10
        orientation: "vertical"
        MDLabel:
            text: "Customer Registration"
            color:  0, 0, 0, 0.9
            font_name: "Comic"
            font_style: 'Button'
            font_size: 25
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15
        TextInput:
            id: fname
            hint_text: "Name"
            multiline: False
            font_name: "Comic"
            icon_right: "account"
            mode: "round"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            normal_color : [1,1,0,1]
        TextInput:
            id: email
            mode: "round"
            hint_text: "Email"
            multiline: False
            font_name: "Comic"
            icon_right: "email"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: phone
            mode: "round"
            hint_text: "Phone"
            font_name: "Comic"
            icon_right: "phone"
            multiline: False
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: password
            mode: "round"
            hint_text: "Password"
            multiline: False
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
            on_text: self.text = self.text.replace(" ", "")
        TextInput:
            id: address
            mode: "round"
            hint_text: "Address"
            multiline: False
            font_name: "Comic"
            icon_right: "address"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: longitude
            mode: "round"
            hint_text: "Longitude"
            multiline: False
            font_name: "Comic"
            icon_right: "longitude"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: latitude
            mode: "round"
            hint_text: "Latitude"
            multiline: False
            font_name: "Comic"
            icon_right: "latitude"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        MDRoundFlatButton:
            text: "REGISTER"
            pos_hint: {"center_x": .5}
            font_size: 20
            on_press: root.send_data()
        Widget:
            size_hint_y: None
            size_hint_y: None
            height: 15
        MDRoundFlatButton:
            text: "Go to Customer Login Page"
            pos_hint: {"center_x": .5}
            font_size: 20
            on_press: root.manager.current='menu'

<ServiceProviderReg>
    name: 'serviceproviderreg'
    sname : sname
    email : email
    password : password
    phone : phone
    address : address

    MDCard:
        size_hint: None,None
        size: 500,550
        pos_hint: {"center_x":.5,"center_y":.5}
        elevation: 5
        md_bg_color: [120, 120, 120]
        padding: 6
        spacing: 9
        orientation: "vertical"
        MDLabel:
            text: "Service Provider Registration"
            color:  0, 0, 0, 0.9
            font_name: "Comic"
            font_style: 'Button'
            font_size: 25
            halign: "center"
            size_hint_y: None
            height: self.texture_size[1]
            padding_y: 15
        TextInput:
            id: sname
            hint_text: "Name"
            font_name: "Comic"
            icon_right: "account"
            mode: "round"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            normal_color : [1,1,0,1]
        TextInput:
            id: email
            mode: "round"
            hint_text: "Email"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: password
            mode: "round"
            hint_text: "Password"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
            password: True
            on_text: self.text = self.text.replace(" ", "")
        TextInput:
            id: phone
            mode: "round"
            hint_text: "Phone"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        TextInput:
            id: address
            mode: "round"
            hint_text: "Address"
            font_name: "Comic"
            icon_right: "eye-off"
            size_hint_x: None
            width: 290
            font_size: 20
            pos_hint: {"center_x": .5}
            color_active: [1,1,1,1]
        Widget:
            size_hint_y: None
            height: 19
        BoxLayout:
            size_hint: .85, None
            height: "30dp"
            pos_hint: {'center_x':.5, 'center_y':.3}
            spacing: "5dp"
            MDFlatButton:
                id: profile
                text: "Profile"
                size_hint_x: 2
                font_size: 20
                md_bg_color: 1, 0, 0, 1
                on_press : root.profile_button()
            Image:
                id : profile_img
            MDFlatButton
                id: licence
                text: "Licence"
                size_hint_x: 2
                font_size: 20
                md_bg_color: 1, 0, 0, 1
                on_press : root.licence_button()
            Image:
                id : licence_img
            MDFlatButton:
                id: idproof
                text: "ID Proof"
                size_hint_x: 2
                font_size: 20
                md_bg_color: 1, 0, 0, 1
                on_press : root.id_proof_button()
            Image:
                id : id_proof_img
        Widget:
            size_hint_y: None
            height: 19
        MDRoundFlatButton:
            text: "REGISTER"
            pos_hint: {"center_x": .5}
            spacing: 9
            font_size: 20
            on_press : root.register_data()
        Widget:
            size_hint_y: None
            height: 15
        MDRoundFlatButton:
            text: "Go to Service Provider Login Page"
            pos_hint: {"center_x": .5}
            font_size: 20
            on_press: root.manager.current='menu'

<AdminScreen>
    name: 'adminmenu'
    location_name : location_name
    longitude : longitude
    latitude : latitude
    category_name : category_name
    MDBottomNavigation:
        md_bg_color:43/255,135/255,168/255,1
        MDBottomNavigationItem:
            name: "screen6"
            text: "Locations"
            font_name: "Comic"
            font_size: 5
            MDCard:
                size_hint: None,None
                size: 450,460
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 9
                spacing: 5
                orientation: "vertical"
                MDTextField:
                    id : location_name
                    hint_text: "Location Name"
                    font_name: "Comic"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                    normal_color : [1,1,0,1]
                MDTextField:
                    id : longitude
                    hint_text: "Longitude"
                    font_name: "Comic"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                MDTextField:
                    id : latitude
                    hint_text: "Latitude"
                    font_name: "Comic"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                MDRoundFlatButton:
                    id: location_picture
                    text: "Select Location Picture"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    md_bg_color: 1, 0, 0, 1
                    on_press : root.location_button()
                Image:
                    id : location_picture
                MDRoundFlatButton:
                    text: "ADD LOCATION"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.add_location_data()
                MDRoundFlatButton:
                    text: "View Locations"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.view_locations()
        MDBottomNavigationItem:
            name: "screen8"
            text: "Providers"
            font_name: "Comic"
            font_size: 5
            cols: 9  # Set the number of columns
            ScrollView:
                GridLayout:
                    id: provider_table_layout
                    cols: 9
                    spacing: dp(10)  # Using density-independent pixels for spacing
                    padding: dp(10)  # Using density-independent pixels for padding
                    row_default_height: '10dp'
                    MDLabel:
                        text: 'Provider Name'
                    MDLabel:
                        text: 'Provider Email'
                    MDLabel:
                        text: 'Provider Phone'
                    MDLabel:
                        text: 'Provider Password'
                    MDLabel:
                        text: 'Provider Address'
                    MDLabel:
                        text: 'Profile'
                    MDLabel:
                        text: 'Licence'
                    MDLabel:
                        text: 'ID Proof'
                    MDLabel:
                        text: 'Status'
        MDBottomNavigationItem:
            name: "screen9"
            text: "Categories"
            font_name: "Comic"
            font_size: 5
            MDCard:
                size_hint: None,None
                size: 450,550
                pos_hint: {"center_x":.5,"center_y":.5}
                elevation: 5
                md_bg_color: [120, 120, 120]
                padding: 20
                spacing: 30
                orientation: "vertical"
                MDLabel:
                    text: "ADD CATEGORY"
                    color:  0, 0, 0, 0.9
                    font_name: "Comic"
                    font_style: 'Button'
                    font_size: 40
                    halign: "center"
                    size_hint_y: None
                    height: self.texture_size[1]
                    padding_y: 15
                MDTextField:
                    id : category_name
                    hint_text: "Category Name"
                    font_name: "Comic"
                    size_hint_x: None
                    width: 290
                    font_size: 20
                    pos_hint: {"center_x": .5}
                    color_active: [1,1,1,1]
                MDRoundFlatButton:
                    id: category_picture
                    text: "Select Category Picture"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    md_bg_color: 1, 0, 0, 1
                    on_press : root.category_button()
                Image:
                    id : category_image
                MDRoundFlatButton:
                    text: "ADD CATEGORY"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.add_category_data()
                MDRoundFlatButton:
                    text: "View Category"
                    pos_hint: {"center_x": .5}
                    font_size: 20
                    on_press: root.view_category()
                Widget:
                    size_hint_y: None
                    height: 30
        MDBottomNavigationItem:
            name: "screen11"
            text: "Home"
            font_name: "Comic"
            font_size: 5
            MDRoundFlatButton:
                text: "BACK TO HOME"
                pos_hint: {"center_x": .5}
                font_size: 20
                on_press: root.manager.current='menu'
<SelectableButton>:
    # Draw a background to indicate selection
    canvas.before:
        Color:
            rgba: (.0, 0.9, .1, .3) if self.selected else (0, 0, 0, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    on_press:
        root.var.populate_fields(self)

<ViewLocations>:
    name: 'viewlocations'
    cols: 4  # Set the number of columns
    ScrollView:
        GridLayout:
            id: location_table_layout
            cols: 4
            row_default_height: '30dp'
            MDLabel:
                text: 'Location Name'
            MDLabel:
                text: 'Longitude'
            MDLabel:
                text: 'Latitude'
            MDLabel:
                text: 'Image'
    MDRoundFlatButton:
        text: "Go to Locations Screen"
        pos_hint: {"center_x": .5}
        font_size: 20
        on_press: root.manager.current='adminmenu'

<ViewCategory>:
    name: 'viewcategory'
    cols: 2  # Set the number of columns
    ScrollView:
        GridLayout:
            id: category_table_layout
            cols: 2
            MDLabel:
                text: 'Category Name'
            MDLabel:
                text: 'Image'
    MDRoundFlatButton:
        text: "Go to Category Screen"
        pos_hint: {"center_x": .5}
        font_size: 20
        on_press: root.manager.current='adminmenu'
"""

class TopPage(Screen):
    pass


class MenuScreen(Screen):

    def admin_login(self):
        admin_email = self.admin_email.text
        admin_password = self.admin_password.text
        if admin_email == 'admin@gmail.com' and admin_password == 'admin':
            self.manager.current = 'adminhome'
            toast("Login Successfull")
        else:
            toast("Invalid Login Details")

        self.admin_email.text = ''
        self.admin_password.text = ''

class AdminHome(Screen):
    pass

class AdminScreen(Screen):
    location_name = ObjectProperty(None)
    longitude = ObjectProperty(None)
    latitude = ObjectProperty(None)
    category_name = ObjectProperty(None)

    def add_location_data(self):
        location_name = self.location_name.text
        longitude = self.longitude.text
        latitude = self.latitude.text
        location_picture = self.ids.location_picture.source
        location_file_name = os.path.basename(location_picture)
        s3_client.upload_file(location_picture, Bucket_Name, location_file_name)
        bucket_name = 'mobileappbucket-new'
        s3_file_name = location_file_name

        location_image_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_file_name}'
        count = cursor.execute("select * from location where location_name = '" + str(location_name) + "'")
        if count == 0:
            query = ("insert into location(location_name,longitude,latitude,location_picture) values('" + str(location_name) + "' , '" + str(longitude) + "' , '" + str(latitude) + "' , '" + str(location_image_url) + "')")
            cursor.execute(query)
            conn.commit()
            toast("Location Added Successfull")
        else:
            toast("Duplicate Details")

        self.location_name.text = ''
        self.longitude.text = ''
        self.latitude.text = ''
        self.ids.location_picture.source = ''

    def location_button(self):
        from plyer import filechooser
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        self.ids.location_picture.source = selection[0]
        toast("Location Picture Selected")

    def view_locations(self):
        self.manager.current = "viewlocations"

    def add_category_data(self):
        category_name = self.category_name.text
        category_picture = self.ids.category_image.source
        category_file_name = os.path.basename(category_picture)
        s3_client.upload_file(category_picture, Bucket_Name, category_file_name)
        bucket_name = 'mobileappbucket-new'
        s3_file_name = category_file_name

        category_image_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_file_name}'
        count = cursor.execute("select * from category where category_name = '" + str(category_name) + "'")
        if count == 0:
            query = ("insert into category(category_name,category_picture) values('" + str(category_name) + "' , '" + str(category_image_url) + "')")
            cursor.execute(query)
            conn.commit()
            toast("Category Added Successfull")
        else:
            toast("Duplicate Details")

        self.category_name.text = ''
        self.ids.category_picture.source = ''

    def category_button(self):
        from plyer import filechooser
        filechooser.open_file(on_selection=self.category_selected)

    def category_selected(self, selection):
        self.ids.category_image.source = selection[0]
        toast("Category Image Selected")

    def view_category(self):
        self.manager.current = "viewcategory"

    def __init__(self, **kwargs):
        super(AdminScreen, self).__init__(**kwargs)
        Clock.schedule_once(self.populate_table)

    def populate_table(self, *args):
        self.cols = 2
        provider_table_layout = self.ids['provider_table_layout']
        cursor.execute("SELECT name,email,phone,password,address,profile_picture,license,id_proof,status FROM service_provider")
        service_providers = cursor.fetchall()
        for service_provider in service_providers:
            name = service_provider[0]
            email = service_provider[1]
            phone = service_provider[2]
            password = service_provider[3]
            address = service_provider[4]
            profile_picture = service_provider[5]
            license = service_provider[6]
            id_proof = service_provider[7]
            status = service_provider[8]

            name = MDLabel(text=name)
            email = MDLabel(text=email)
            phone = MDLabel(text=phone)
            password = MDLabel(text=password)
            address = MDLabel(text=address)
            profile_picture = AsyncImage(source=profile_picture)  # Create a new AsyncImage
            license = AsyncImage(source=license)
            id_proof = AsyncImage(source=id_proof)
            status = MDLabel(text=status)

            provider_table_layout.add_widget(name)
            provider_table_layout.add_widget(email)
            provider_table_layout.add_widget(phone)
            provider_table_layout.add_widget(password)
            provider_table_layout.add_widget(address)
            provider_table_layout.add_widget(profile_picture)
            provider_table_layout.add_widget(license)
            provider_table_layout.add_widget(id_proof)
            provider_table_layout.add_widget(status)

class ViewLocations(Screen):
    def __init__(self, **kwargs):
        super(ViewLocations, self).__init__(**kwargs)
        Clock.schedule_once(self.populate_table)

    def populate_table(self, *args):
        self.cols = 4
        try:
            location_table_layout = self.ids['location_table_layout']
            cursor.execute("SELECT location_name,longitude,latitude,location_picture FROM location")
            locations = cursor.fetchall()
            for location in locations:
                location_name = location[0]
                longitude = location[1]
                latitude = location[2]
                location_picture = location[3]

                location_name = MDLabel(text=location_name)
                longitude = MDLabel(text=longitude)
                latitude = MDLabel(text=latitude)
                location_picture = AsyncImage(source=location_picture)

                location_table_layout.add_widget(location_name)
                location_table_layout.add_widget(longitude)
                location_table_layout.add_widget(latitude)
                location_table_layout.add_widget(location_picture)
        except Exception as e:
            print(f"An error occurred: {e}")

class ViewCategory(Screen):
    def __init__(self, **kwargs):
        super(ViewCategory, self).__init__(**kwargs)
        Clock.schedule_once(self.populate_table)

    def populate_table(self, *args):
        self.cols = 2
        category_table_layout = self.ids['category_table_layout']
        cursor.execute("SELECT category_name,category_picture FROM category")
        categories = cursor.fetchall()
        for category in categories:
            category_name = category[0]
            category_picture_path = category[1]

            category_name_label = MDLabel(text=category_name)
            category_image = AsyncImage(source=category_picture_path,size=(30, 30))  # Create a new AsyncImage

            category_table_layout.add_widget(category_name_label)
            category_table_layout.add_widget(category_image)


class CustomerRegistration(Screen):

    fname = ObjectProperty(None)
    email= ObjectProperty(None)
    phone= ObjectProperty(None)
    password= ObjectProperty(None)
    address= ObjectProperty(None)
    longitude= ObjectProperty(None)
    latitude= ObjectProperty(None)

    def send_data(self):
        fname = self.fname.text
        email =  self.email.text
        phone =  self.phone.text
        password =  self.password.text
        address =  self.address.text
        longitude =  self.longitude.text
        latitude = self.latitude.text
        count = cursor.execute("select * from customer where email = '"+str(email)+"' or phone = '"+str(phone)+"'")
        if count == 0:
            query = ("insert into customer(name,email,phone,password,address,longitude,latitude) values('" + str(fname) + "' , '" + str(email) + "' , '" + str(phone) + "' , '" + str(password) + "' , '" + str(address) + "' , '" + str(longitude) + "' , '" + str(latitude) + "')")
            cursor.execute(query)
            conn.commit()
            toast("Registration Successfull")
        else:
            toast("Duplicate Details")
        self.fname.text = ''
        self.email.text = ''
        self.phone.text = ''
        self.password.text = ''
        self.address.text = ''
        self.longitude.text = ''
        self.latitude.text = ''


class ServiceProviderReg(Screen):

    sname = ObjectProperty(None)
    email = ObjectProperty(None)
    phone = ObjectProperty(None)
    password = ObjectProperty(None)
    address = ObjectProperty(None)

    def register_data(self):
        sname = self.sname.text
        email = self.email.text
        phone = self.phone.text
        password = self.password.text
        address = self.address.text
        profile = self.ids.profile_img.source
        license = self.ids.licence_img.source
        idproof = self.ids.id_proof_img.source
        profile_file_name = os.path.basename(profile)
        license_file_name = os.path.basename(license)
        idproof_file_name = os.path.basename(idproof)
        s3_client.upload_file(profile, Bucket_Name, profile_file_name)
        s3_client.upload_file(license, Bucket_Name, license_file_name)
        s3_client.upload_file(idproof, Bucket_Name, idproof_file_name)
        bucket_name = 'mobileappbucket-new'
        s3_file_name = profile_file_name
        s3_file_name_license = license_file_name
        s3_file_name_idproof = idproof_file_name

        profile_image_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_file_name}'
        license_image_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_file_name_license}'
        idproof_image_url = f'https://{bucket_name}.s3.amazonaws.com/{s3_file_name_idproof}'
        count = cursor.execute("select * from service_provider where email = '" + str(email) + "' or phone = '" + str(phone) + "'")
        if count == 0:
            query = ("insert into service_provider(name,email,phone,password,address,profile_picture,license,id_proof,status) values('" + str(sname) + "' , '" + str(email) + "' , '" + str(phone) + "' , '" + str(password) + "' , '" + str(address) + "' , '" + str(profile_image_url) + "' , '" + str(license_image_url) + "' , '" + str(idproof_image_url) + "' , 'Deactivate')")
            cursor.execute(query)
            conn.commit()
            toast("Registration Successfull")
        else:
            toast("Duplicate Details")
        self.sname.text = ''
        self.email.text = ''
        self.phone.text = ''
        self.password.text = ''
        self.address.text = ''
        self.ids.profile_img.source = ''
        self.ids.licence_img.source = ''
        self.ids.id_proof_img.source = ''

    def profile_button(self):
        from plyer import filechooser
        filechooser.open_file(on_selection = self.selected)

    def selected(self, selection):
        self.ids.profile_img.source = selection[0]
        toast("Profile Selected")

    def licence_button(self):
        from plyer import filechooser
        filechooser.open_file(on_selection = self.licence_selected)

    def licence_selected(self, selection):
        self.ids.licence_img.source = selection[0]
        toast("Licence Uploaded")

    def id_proof_button(self):
        from plyer import filechooser
        filechooser.open_file(on_selection = self.id_proof_selected)

    def id_proof_selected(self, selection):
        self.ids.id_proof_img.source = selection[0]
        toast("ID Proof Selected")


class MainApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Snow Removal App"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_string(screen_helper)
        self.manager = ScreenManager(transition=NoTransition())
        self.manager.add_widget(TopPage(name="toppage"))
        self.manager.add_widget(MenuScreen(name="menu"))
        self.manager.add_widget(CustomerRegistration(name="c    ustomerreg"))
        self.manager.add_widget(ServiceProviderReg(name="serviceproviderreg"))
        self.manager.add_widget(AdminHome(name="adminhome"))
        self.manager.add_widget(AdminScreen(name="adminmenu"))
        self.manager.add_widget(ViewLocations(name="viewlocations"))
        self.manager.add_widget(ViewCategory(name="viewcategory"))

    def customerreg(self):
        self.manager.current = "customerreg"

    def serviceproviderreg(self):
        self.manager.current = "serviceproviderreg"

    def viewlocations(self):
        self.manager.current = "viewlocations"

    def viewcategory(self):
        self.manager.current = "viewcategory"



if __name__ == "__main__":
    MainApp().run()