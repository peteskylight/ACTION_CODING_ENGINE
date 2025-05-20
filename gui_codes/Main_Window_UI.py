# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MAIN_WINDOW - FINAL LAYOUTAcVSIR.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGraphicsView, QGridLayout, QGroupBox,
    QHeaderView, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

from utils import MultiSelectComboBox
import icons_rc
import icons_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1340, 720)
        MainWindow.setMinimumSize(QSize(1340, 720))
        MainWindow.setMaximumSize(QSize(1340, 720))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons_resource/ACE Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #f5f5f5;\n"
"    color: #212529;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QSlider {\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLabel#label_34, #label_25, #ai_analytics_label, #label_66, #label_65, #label_52,#label_54, #Homepage_label{\n"
"	font-family: 'Bell MT';\n"
"	font-size: 45px;\n"
"	font-weight: 500;\n"
"    padding: 6px 12px;\n"
"	color: #B60019;\n"
"	background-color: transparent;\n"
"	border-bottom: 1px solid red;\n"
"}\n"
"\n"
"QLabel#label_27 {\n"
"	font-family: 'Bell MT';\n"
"	font-size: 36px;\n"
"    font-weight: 500;\n"
"    padding: 6px 12px;\n"
"	color: #B60019;\n"
"	background-color: transparent;\n"
"	border-bottom: 1px solid red;\n"
"}\n"
"\n"
"QLabel#label_35, #label_38, #label_26, #label_69,#interval_time_label_advanced_analytics,#interval_time_label,#label_7,#label_16,#label_19{\n"
"	font-family: 'Segoe UI';\n"
"	font-size: 15px;\n"
"    padding: 6px 12px;\n"
"	background-color: transparent;\n"
"}\n"
""
                        "\n"
"QLabel#label_23, #label_24, #label_18,#label_68, #label_79,#label_78,#label_77,#label_80,#CenterPlacement_label_2,#FrontPlacement_label_2,#label_48,#label_49,#label_50,#label_51,#label_82,#label_81,#label_29,#label_30,#label_46,#label_47,#label_71,#label_70,#CenterPlacement_label_3,#FrontPlacement_label_3,#label_72,#label_75,#label_73,#label_74 , #TimeLabel,#TimeLabel_2,#label_Camera,#label_10,#label_9,#label_5,#label_6{\n"
"	font-family: 'Segoe UI';\n"
"	font-size: 14px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLabel#label_15{\n"
"	background-color: #B60019;  /* Default background */\n"
"    color: white;               /* Text color */    \n"
"	border: 1px solid #e0a800; /* Slightly darker border */\n"
"    border-radius: 5px;\n"
"	font-family: 'Segoe UI';\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QLabel#label_17{\n"
"	background-color: #B60019;  /* Default background */\n"
"    color: white;               /* Text color */    \n"
"	border: 1px solid #e0a800; /* Slightly darker border */\n"
"    bor"
                        "der-radius: 5px;\n"
"	font-family: 'Segoe UI';\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QLabel#video_preview_label_center{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#video_preview_label_front{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#video_preview_label_ai_analytics_center{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#video_preview_label_ai_analytics_front{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
" "
                        "   background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#ai_analytics_preview_front{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#ai_analytics_preview_center{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#ai_analytics_table_event_logs_preview_front{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#ai_analytics_"
                        "table_event_logs_preview_center{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#ai_analytics_chunk_summary_preview_front{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#ai_analytics_chunk_summary_preview_center{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#advanced_analytics_heatmap_preview_center{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding"
                        ": 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#advanced_analytics_heatmap_preview_front{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#adv_analytics_preview_line_graph_front{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#adv_analytics_preview_line_graph_center{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#adv_analytics_preview_event_logs_table_front{\n"
"	 border"
                        ": 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#adv_analytics_preview_event_logs_table_center{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#advanced_analytics_chunk_summary_preview_front{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#advanced_analytics_chunk_summary_preview_center{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated s"
                        "hadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#white_frame_feed{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#camera_feed{\n"
"	 border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    background-color: #F9F6EE; /* soft warm tone */\n"
"    padding: 5px;\n"
"    /* Simulated shadow */\n"
"    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QLabel#session_name_label, #day_label,#label_45, #label_33, #label_36, #label_37, #label_39, #label_41, #label_42, #label_43, #label_44, #ai_analytics_count_students, #ai_analytics_count_left_arm_extending_sidewards, #ai_analytics_count_right_arm_extending_sidewards, #ai_analytics_count_facing_downwards, #ai_analytics_count_facing_forward, #ai_analytics_count_facing_forward, #ai_analytics_count_facing_right, #ai_analytics_coun"
                        "t_sitting, #ai_analytics_count_standing,#label_76,#label_60,#label_61,#label_62,#label_53,#label_63,#label_64,#label_56,#label_59,#label_57,#label_58,#advanced_analytics_count_students,#advanced_analytics_count_left_arm_extending_sidewards,#advanced_analytics_count_left_arm_neutral,#advanced_analytics_count_left_arm_unknown,#advanced_analytics_count_right_arm_extending_sidewards,#advanced_analytics_count_right_arm_neutral,#advanced_analytics_count_right_arm_unknown,#advanced_analytics_count_facing_downwards,#advanced_analytics_count_facing_forward,#advanced_analytics_count_facing_left,#advanced_analytics_count_facing_right\n"
"{\n"
"	font-family: 'Segoe UI';\n"
"	font-size: 14px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLabel#label_55,#label_72,#label_79{\n"
"	font-family:'Segoe UI';\n"
"	font-size:14px;\n"
" 	background-color: #B60019;  /* Default background */\n"
"    color: white;               /* Text color */    \n"
"	border: 1px solid #e0a800; /* Slightly darker border */\n"
"    border-radius"
                        ": 5px;\n"
"}\n"
"QLabel #tentlogo2{\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton {\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 6px;\n"
"    padding: 6px 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e0e0e0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #cccccc;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    padding: 4px;\n"
"    background-color: #fff8dc; \n"
"    color: black;\n"
"    font-family: 'Segoe UI';\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid #e0a800;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"    background-color: #fff8dc; /* light warm tone */\n"
"    color: #333;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid #d39e00;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    widt"
                        "h: 20px;\n"
"    border-left: 1px solid #e0a800;\n"
"    background-color: #e0a800;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/arrow-217-256.png); /* Optional: use your own icon */\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #fffef0;\n"
"    selection-background-color: #fdd835;\n"
"    border: 1px solid #e0a800;\n"
"}\n"
"\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid #dddddd;\n"
"    border-radius: 6px;\n"
"    margin-top: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 6px;\n"
"    color: #495057;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #212529; /* Dark label text */\n"
"    background-color: transparent;\n"
"    spacing: 5px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"    border: 1px solid #bf001b;\n"
"    border-radius: 3px;\n"
"    background-color: #ffffff;\n"
""
                        "}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/icons/check-mark.png); /* Replace with your icon path */\n"
"    background-color: #ffffff;\n"
"    border: 1px solid #bf001b;\n"
"}\n"
"\n"
"\n"
"QPushButton#Home_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffffff, stop: 1 #f7f7f7\n"
"    );\n"
"    color: #B60019;\n"
"    border: 1px solid #990018;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"    font-size: 15px;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"    qproperty-iconSize: 20px;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton#Home_button:hover{\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #fff2f2, stop: 1 #ffeaea\n"
"    );\n"
"    border: 1px solid #B60019;\n"
"    color: #B60019;\n"
"}\n"
"\n"
"QPushButton#Home_button:pressed{\n"
"    background-color: #f1d6d6;\n"
"    border: 1px solid #7a0012;\n"
"    padding-top: 9px; pa"
                        "dding-bottom: 7px; /* Subtle press-down effect */\n"
"}\n"
"\n"
"QPushButton#Home_button:checked{\n"
"    background-color: #ffd6d9;\n"
"    color: #900012;\n"
"    border: 2px solid #B60019;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#Import_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffffff, stop: 1 #f7f7f7\n"
"    );\n"
"    color: #B60019;\n"
"    border: 1px solid #990018;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"    font-size: 15px;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"    qproperty-iconSize: 20px;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton#Import_button:hover{\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #fff2f2, stop: 1 #ffeaea\n"
"    );\n"
"    border: 1px solid #B60019;\n"
"    color: #B60019;\n"
"}\n"
"\n"
"QPushButton#Import_button:pressed{\n"
"    background-color: #f1d6d6;\n"
"    border: 1px solid #7a0012"
                        ";\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"}\n"
"\n"
"QPushButton#Import_button:checked{\n"
"    background-color: #ffd6d9;\n"
"    color: #900012;\n"
"    border: 2px solid #B60019;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#AI_analytics_button{\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffffff, stop: 1 #f7f7f7\n"
"    );\n"
"    color: #B60019;\n"
"    border: 1px solid #990018;\n"
"    border-radius: 8px;\n"
"    font-size: 15px;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"    qproperty-iconSize: 20px;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton#AI_analytics_button:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #fff2f2, stop: 1 #ffeaea\n"
"    );\n"
"    border: 1px solid #B60019;\n"
"    color: #B60019;\n"
"}\n"
"\n"
"QPushButton#AI_analytics_button:pressed {\n"
"    background-color: #f1d6d6;\n"
"    b"
                        "order: 1px solid #7a0012;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"}\n"
"\n"
"QPushButton#AI_analytics_button:checked{\n"
"    background-color: #ffd6d9;\n"
"    color: #900012;\n"
"    border: 2px solid #B60019;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#Advanced_analytics_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffffff, stop: 1 #f7f7f7\n"
"    );\n"
"     color: #B60019;\n"
"    border: 1px solid #990018;\n"
"    border-radius: 8px;\n"
"    font-size: 15px;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"    qproperty-iconSize: 20px;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton#Advanced_analytics_button:hover{\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #fff2f2, stop: 1 #ffeaea\n"
"    );\n"
"    border: 1px solid #B60019;\n"
"    color: #B60019;\n"
"}\n"
"\n"
"QPushButton#Advanced_analytics_button:press"
                        "ed{\n"
"    background-color: #f1d6d6;\n"
"    border: 1px solid #7a0012;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"}\n"
"\n"
"QPushButton#Advanced_analytics_button:checked{\n"
"    background-color: #ffd6d9;\n"
"    color: #900012;\n"
"    border: 2px solid #B60019;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#Export_file_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffffff, stop: 1 #f7f7f7\n"
"    );\n"
"    color: #B60019;\n"
"    border: 1px solid #990018;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"    font-size: 15px;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"    qproperty-iconSize: 20px;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton#Export_file_button:hover{\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #fff2f2, stop: 1 #ffeaea\n"
"    );\n"
"    border: 1px solid #B60019;\n"
"    color: #"
                        "B60019;\n"
"}\n"
"\n"
"QPushButton#Export_file_button:pressed {\n"
"    background-color: #f1d6d6;\n"
"    border: 1px solid #7a0012;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"}\n"
"\n"
"QPushButton#Export_file_button:checked {\n"
"    background-color: #ffd6d9;\n"
"    color: #900012;\n"
"    border: 2px solid #B60019;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#Tutorial_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffffff, stop: 1 #f7f7f7\n"
"    );\n"
"    color: #B60019;\n"
"    border: 1px solid #990018;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"    font-size: 15px;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"    qproperty-iconSize: 20px;\n"
"}\n"
"\n"
"QPushButton#Tutorial_button:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #fff2f2, stop: 1 #ffeaea\n"
"    );\n"
"    border: 1px solid #B60019;\n"
""
                        "    color: #B60019;\n"
"}\n"
"\n"
"QPushButton#Tutorial_button:pressed {\n"
"    background-color: #fce7e8;\n"
"    border: 1px solid #7a0012;\n"
"    padding-top: 9px;\n"
"    padding-bottom: 7px;\n"
"    color: #B60019;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#Tutorial_button:checked {\n"
"    background-color: #fce7e8;\n"
"    border: 2px solid #B60019;\n"
"    font-weight: bold;\n"
"    color: #B60019;\n"
"}\n"
"\n"
"QPushButton#Exit_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffffff, stop: 1 #f7f7f7\n"
"    );\n"
"    color: #B60019;\n"
"    border: 1px solid #990018;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"    font-size: 15px;\n"
"    font-weight: 500;\n"
"    text-align: left;\n"
"    qproperty-iconSize: 20px;\n"
"}\n"
"\n"
"QPushButton#Exit_button:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #fff2f2, stop: 1 #ffeaea\n"
"    );\n"
"    bor"
                        "der: 1px solid #B60019;\n"
"    color: #B60019;\n"
"}\n"
"\n"
"QPushButton#Exit_button:pressed {\n"
"    background-color: #fce7e8;\n"
"    border: 1px solid #7a0012;\n"
"    padding-top: 9px;\n"
"    padding-bottom: 7px;\n"
"    color: #B60019;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton#Exit_button:checked {\n"
"    background-color: #fce7e8;\n"
"    border: 2px solid #B60019;\n"
"    font-weight: bold;\n"
"    color: #B60019;\n"
"}\n"
"\n"
"QPushButton#play_pause_button__ai_analytics_line_graph {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #43d77a, stop: 1 #34c065\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #2dab57;\n"
"    border-radius: 8px;\n"
"    font-size: 18px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QPushButton#play_pause_button__ai_analytics_line_graph:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y"
                        "2: 1,\n"
"        stop: 0 #6fe89a, stop: 1 #43d77a\n"
"    );\n"
"    box-shadow: 0px 4px 8px rgba(52, 192, 101, 0.3);\n"
"}\n"
"\n"
"QPushButton#play_pause_button__ai_analytics_line_graph:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #34c065, stop: 1 #2aa254\n"
"    );\n"
"    border: 1px solid #248c47;\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#play_pause_button__ai_analytics_line_graph:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FFD666, stop: 1 #FFB60A\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #e0a800;\n"
"    box-shadow: 0px 4px 8px rgba(255, 182, 10, 0.4);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_ai_analytics_table_event_logs {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #43d77a, stop: 1 #34c065\n"
"    );\n"
"    color: white;\n"
"    border: 1px soli"
                        "d #2dab57;\n"
"    border-radius: 8px;\n"
"    font-size: 18px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_ai_analytics_table_event_logs:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #6fe89a, stop: 1 #43d77a\n"
"    );\n"
"    box-shadow: 0px 4px 8px rgba(52, 192, 101, 0.3);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_ai_analytics_table_event_logs:pressed {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #34c065, stop: 1 #2aa254\n"
"    );\n"
"    border: 1px solid #248c47;\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton #play_pause_button_ai_analytics_table_event_logs:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FFD666, stop: 1 #FFB60A\n"
"    );\n"
"    color: white;\n"
"    border:"
                        " 1px solid #e0a800;\n"
"    box-shadow: 0px 4px 8px rgba(255, 182, 10, 0.4);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_video_preview {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #43d77a, stop: 1 #34c065\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #2dab57;\n"
"    border-radius: 8px;\n"
"    font-size: 18px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_video_preview:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #6fe89a, stop: 1 #43d77a\n"
"    );\n"
"    box-shadow: 0px 4px 8px rgba(52, 192, 101, 0.3);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_video_preview:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #34c065, stop: 1 #2aa254\n"
"    );\n"
"    border: 1px solid #248c47;\n"
"    box-shadow: inset "
                        "0px 2px 4px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_video_preview:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FFD666, stop: 1 #FFB60A\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #e0a800;\n"
"    box-shadow: 0px 4px 8px rgba(255, 182, 10, 0.4);\n"
"}\n"
"\n"
"QPushButton#ai_analytics_event_summary_play_pause_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #43d77a, stop: 1 #34c065\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #2dab57;\n"
"    border-radius: 10px;\n"
"    font-size: 18px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QPushButton#ai_analytics_event_summary_play_pause_button:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #6fe89a, stop: 1 #43d77a\n"
"    );\n"
"    box-shadow: 0p"
                        "x 4px 8px rgba(52, 192, 101, 0.3);\n"
"}\n"
"\n"
"QPushButton#ai_analytics_event_summary_play_pause_button:pressed {\n"
"     background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #34c065, stop: 1 #2aa254\n"
"    );\n"
"    border: 1px solid #248c47;\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#ai_analytics_event_summary_play_pause_button:checked {\n"
"  background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FFD666, stop: 1 #FFB60A\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #e0a800;\n"
"    box-shadow: 0px 4px 8px rgba(255, 182, 10, 0.4);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_ai_analytics_heatmap {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #43d77a, stop: 1 #34c065\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #2dab57;\n"
"    border-radius: 10px;\n"
"    font-size: 18px;\n"
"    padding: 8px 16p"
                        "x;\n"
"    font-weight: 600;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_ai_analytics_heatmap:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #6fe89a, stop: 1 #43d77a\n"
"    );\n"
"    box-shadow: 0px 4px 8px rgba(52, 192, 101, 0.3);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_ai_analytics_heatmap:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #34c065, stop: 1 #2aa254\n"
"    );\n"
"    border: 1px solid #248c47;\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_ai_analytics_heatmap:checked {\n"
"     background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FFD666, stop: 1 #FFB60A\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #e0a800;\n"
"    box-shadow: 0px 4px 8px rgba(255, 182, 10, 0.4);\n"
"}\n"
"\n"
"QPushButton#play_pau"
                        "se_button_advanced_analytics_heatmap {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #43d77a, stop: 1 #34c065\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #2dab57;\n"
"    border-radius: 10px;\n"
"    font-size: 18px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_advanced_analytics_heatmap:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #6fe89a, stop: 1 #43d77a\n"
"    );\n"
"    box-shadow: 0px 4px 8px rgba(52, 192, 101, 0.3);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_advanced_analytics_heatmap:pressed {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #34c065, stop: 1 #2aa254\n"
"    );\n"
"    border: 1px solid #248c47;\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#play_pause_butt"
                        "on_advanced_analytics_heatmap:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FFD666, stop: 1 #FFB60A\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #e0a800;\n"
"    box-shadow: 0px 4px 8px rgba(255, 182, 10, 0.4);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_advanced_analytics_line_graph {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #43d77a, stop: 1 #34c065\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #2dab57;\n"
"    border-radius: 10px;\n"
"    font-size: 18px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_advanced_analytics_line_graph:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #6fe89a, stop: 1 #43d77a\n"
"    );\n"
"    box-shadow: 0px 4px 8px rgba(52, 192, 101, 0.3);\n"
"}\n"
"\n"
"QPushB"
                        "utton#play_pause_button_advanced_analytics_line_graph:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #34c065, stop: 1 #2aa254\n"
"    );\n"
"    border: 1px solid #248c47;\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_advanced_analytics_line_graph:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FFD666, stop: 1 #FFB60A\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #e0a800;\n"
"    box-shadow: 0px 4px 8px rgba(255, 182, 10, 0.4);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_advanced_analytics_table_event_logs {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #43d77a, stop: 1 #34c065\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #2dab57;\n"
"    border-radius: 10px;\n"
"    font-size: 18px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
" "
                        "   box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_advanced_analytics_table_event_logs:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #6fe89a, stop: 1 #43d77a\n"
"    );\n"
"    box-shadow: 0px 4px 8px rgba(52, 192, 101, 0.3);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_advanced_analytics_table_event_logs:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #34c065, stop: 1 #2aa254\n"
"    );\n"
"    border: 1px solid #248c47;\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#play_pause_button_advanced_analytics_table_event_logs:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FFD666, stop: 1 #FFB60A\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #e0a800;\n"
"    box-shadow: 0px 4px 8px rgba(255, 182, 10, 0.4);\n"
"}\n"
"\n"
"QPushButton"
                        "#advanced_analytics_event_summary_play_pause_button{\n"
"	background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #43d77a, stop: 1 #34c065\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #2dab57;\n"
"    border-radius: 8px;\n"
"    font-size: 18px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QPushButton#advanced_analytics_event_summary_play_pause_button:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FFD666, stop: 1 #FFB60A\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #e0a800;\n"
"    box-shadow: 0px 4px 8px rgba(255, 182, 10, 0.4);\n"
"}\n"
"\n"
"QPushButton#advanced_analytics_event_summary_play_pause_button:pressed {\n"
"	 background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FFB60A, stop: 1 #e69500\n"
"    );\n"
"    border: 1px solid #c77800;\n"
"    box-shadow: in"
                        "set 0px 2px 4px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#advanced_analytics_event_summary_play_pause_button:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #43d77a, stop: 1 #34c065\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #2dab57;\n"
"    box-shadow: 0px 4px 8px rgba(52, 192, 101, 0.3);\n"
"}\n"
"\n"
"QPushButton#Back_to_Home_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 18px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#Back_to_Home_button:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#Back_to_Home_button:pressed {\n"
"    background-co"
                        "lor: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#Back_to_Home_button:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QLabel#CenterPlacement_label_3, #FrontPlacement_label_3,#TimeLabel_2,#TimeLabel,#label_31,#label_32,#CenterPlacement_label_2,#FrontPlacement_label_2,#label_46,#label_47,#label_71,#label_70#label_46,#label_47,#label_71,#label_70,#label_48,#label_49,#label_50,#label_51,#label_81,#label_82,#label_30,#label_29{\n"
"    background-color: #B60019;  /* Default background */\n"
"    color: white;               /* Text color */    \n"
"	border: 1px solid #e0a800; /* Slightly darker borde"
                        "r */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QFrame#frame_15,#frame_14{\n"
"	background-color: #bf001b;\n"
"    border-radius: 10px;\n"
"    color: white;               /* Text color */    \n"
"}\n"
"\n"
"QPushButton#import_video_button_front{\n"
"  background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 15px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#import_video_button_front:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#import_video_button_front:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-"
                        "top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#import_video_button_front:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QPushButton#import_video_button_center {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 15px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#import_video_button_center:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#import_video_button_center:pressed {\n"
"    backgr"
                        "ound-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#import_video_button_center:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QPushButton#openCamera {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 14px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); /* Subtle 3D shadow */\n"
"}\n"
"\n"
"QPushButton#openCamera:hover {\n"
"    background-color: qlineargradient(\n"
""
                        "        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#openCamera:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#openCamera:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QPushButton#closeCamera {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 14px;\n"
"    box-shadow: 0px 4px "
                        "6px rgba(0, 0, 0, 0.2); /* Subtle 3D shadow */\n"
"}\n"
"\n"
"QPushButton#closeCamera:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#closeCamera:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#closeCamera:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QFrame#frame_3{\n"
"	background-color: #efefef;\n"
"    border-radius: 5px;\n"
"    color: white;               /* Text color */    \n"
"}\n"
"\n"
"QFrame#frame_4{\n"
"	background-color: "
                        "#efefef;\n"
"    border-radius: 10px;\n"
"    color: white;               /* Text color */    \n"
"}\n"
"\n"
"QLabel#fps_label{\n"
"	font-family: 'Segoe UI';\n"
"	font-size: 14px;\n"
"	background-color: transparent;\n"
"	color: #E270FF;\n"
"}\n"
"\n"
"QLabel#cpu_label{\n"
"	font-family: 'Segoe UI';\n"
"	font-size: 14px;\n"
"	background-color: transparent;\n"
"	color: #59D2FF;\n"
"}\n"
"\n"
"QLabel#ram_label{\n"
"	font-family: 'Segoe UI';\n"
"	font-size: 14px;\n"
"	background-color: transparent;\n"
"	color: #BF001B;\n"
"}\n"
"\n"
"QLabel#gpu_label{\n"
"	font-family: 'Segoe UI';\n"
"	font-size: 14px;\n"
"	background-color: transparent;\n"
"	color: #45FF6E;\n"
"}\n"
"\n"
"QPushButton#refresh_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 14px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0,"
                        " 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#refresh_button:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#refresh_button:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#refresh_button:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QPushButton#delete_action_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px"
                        " solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 14px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#delete_action_button:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#delete_action_button:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#delete_action_button:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QPushButton#add_action_button {\n"
"   background-color: qlin"
                        "eargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 14px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#add_action_button:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#add_action_button:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#add_action_button:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        s"
                        "top: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QPushButton#recording_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #43d77a, stop: 1 #34c065\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #2dab57;\n"
"    border-radius: 10px;\n"
"    font-size: 25px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.15);\n"
"}\n"
"\n"
"QPushButton#recording_button:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #6fe89a, stop: 1 #43d77a\n"
"    );\n"
"    box-shadow: 0px 4px 8px rgba(52, 192, 101, 0.3);\n"
"}\n"
"\n"
"QPushButton#recording_button:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #34c065, stop: 1 #2aa254\n"
"    );\n"
"    border: 1px solid #248c47;\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushBu"
                        "tton#recording_button:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FFD666, stop: 1 #FFB60A\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #e0a800;\n"
"    box-shadow: 0px 4px 8px rgba(255, 182, 10, 0.4);\n"
"}\n"
"\n"
"QPushButton#browseButton {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 14px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); /* Subtle 3D shadow */\n"
"}\n"
"\n"
"QPushButton#browseButton:hover {\n"
"  background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #C82030, stop: 1 #A3001F\n"
"    );\n"
"}\n"
"\n"
"QPushButton#browseButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, s"
                        "top: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#browseButton:checked {\n"
"  	 background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QPushButton#refresh_action_list {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 14px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); /* Subtle 3D shadow */\n"
"}\n"
"\n"
"QPushButton#refresh_action_list:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
""
                        "}\n"
"\n"
"QPushButton#refresh_action_list:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#refresh_action_list:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QSlider#interval_slider::groove:horizontal {\n"
"    height: 8px;  /* Thickness of the slider track */\n"
"    background: #cccccc;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider#interval_slider::handle:horizontal {\n"
"    width: 20px;  /* Size of the draggable handle */\n"
"    height: 20px;\n"
"    margin: -6px 0; /* Center the handle vertically */\n"
"    background: #B60019;\n"
"    border: 1px s"
                        "olid #900012;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider#sequence_slider::groove:horizontal {\n"
"    height: 8px;  /* Thickness of the slider track */\n"
"    background: #cccccc;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider#sequence_slider::handle:horizontal {\n"
"    width: 20px;  /* Size of the draggable handle */\n"
"    height: 20px;\n"
"    margin: -6px 0; /* Center the handle vertically */\n"
"    background: #B60019;\n"
"    border: 1px solid #900012;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider#ai_analytics_interval_slider_minutes::groove:horizontal {\n"
"    background: #cccccc; /* Track background color */\n"
"    height: 8px;         /* Track thickness */\n"
"    border-radius: 4px;  /* Rounded edges for groove */\n"
"}\n"
"\n"
"QSlider#ai_analytics_interval_slider_minutes::handle:horizontal {\n"
"    background: #B60019; /* Handle color */\n"
"    border: 1px solid #900012; /* Handle border color */\n"
"    width: 15px;         /* Handle width (smaller size) */\n"
"    heigh"
                        "t: 15px;        /* Handle height (smaller size) */\n"
"    margin: -3px 0;      /* Center handle vertically */\n"
"    border-radius: 7px;  /* Make handle perfectly circular */\n"
"}\n"
"\n"
"QSlider#ai_analytics_interval_slider_seconds::groove:horizontal {\n"
"    background: #cccccc; /* Track background color */\n"
"    height: 8px;         /* Track thickness */\n"
"    border-radius: 4px;  /* Rounded edges for groove */\n"
"}\n"
"\n"
"QSlider#ai_analytics_interval_slider_seconds::handle:horizontal {\n"
"    background: #B60019; /* Handle color */\n"
"    border: 1px solid #900012; /* Handle border color */\n"
"    width: 15px;         /* Handle width (smaller size) */\n"
"    height: 15px;        /* Handle height (smaller size) */\n"
"    margin: -3px 0;      /* Center handle vertically */\n"
"    border-radius: 7px;  /* Make handle perfectly circular */\n"
"}\n"
"\n"
"QSlider#advanced_analytics_interval_slider_minutes::groove:horizontal {\n"
"    background: #cccccc; /* Track background color */\n"
"    he"
                        "ight: 8px;         /* Track thickness */\n"
"    border-radius: 4px;  /* Rounded edges for groove */\n"
"}\n"
"\n"
"QSlider#advanced_analytics_interval_slider_minutes::handle:horizontal {\n"
"    background: #B60019; /* Handle color */\n"
"    border: 1px solid #900012; /* Handle border color */\n"
"    width: 15px;         /* Handle width (smaller size) */\n"
"    height: 15px;        /* Handle height (smaller size) */\n"
"    margin: -3px 0;      /* Center handle vertically */\n"
"    border-radius: 7px;  /* Make handle perfectly circular */\n"
"}\n"
"\n"
"QSlider#advanced_analytics_interval_slider_seconds::groove:horizontal {\n"
"    background: #cccccc; /* Track background color */\n"
"    height: 8px;         /* Track thickness */\n"
"    border-radius: 4px;  /* Rounded edges for groove */\n"
"}\n"
"\n"
"QSlider#advanced_analytics_interval_slider_seconds::handle:horizontal {\n"
"    background: #B60019; /* Handle color */\n"
"    border: 1px solid #900012; /* Handle border color */\n"
"    width: 15px;   "
                        "      /* Handle width (smaller size) */\n"
"    height: 15px;        /* Handle height (smaller size) */\n"
"    margin: -3px 0;      /* Center handle vertically */\n"
"    border-radius: 7px;  /* Make handle perfectly circular */\n"
"}\n"
"\n"
"QPushButton#start_button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 18px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#start_button:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#start_button:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding"
                        "-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#start_button:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"\n"
"QPushButton#connect_Button {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 15px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#connect_Button:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#connect_Button:pressed {\n"
"    background-color: qlineargradient(\n"
"        x"
                        "1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#connect_Button:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"\n"
"QPushButton#generate_document_report{\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 15px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#generate_document_report:hover {\n"
"      background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"   "
                        "     stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#generate_document_report:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#generate_document_report:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"\n"
"QPushButton#export_media_button{\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 15px;\n"
"    box-shadow: 0px 4px 6px "
                        "rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#export_media_button:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#export_media_button:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#export_media_button:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QPushButton#generate_document_report_2{\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop: 1 #B60019\n"
"    );\n"
"    color"
                        ": white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 15px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#generate_document_report_2:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#generate_document_report_2:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#generate_document_report_2:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    );\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QLabel#ProjectN"
                        "ame{\n"
"	background-color: transparent;\n"
"	font-size: 17px;\n"
"	font-family: 'Bell MT';\n"
"}\n"
"\n"
"QPushButton#pushButton{\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #D91A30, stop:1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014; /* Slightly darker red border */\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #FFC5CD, stop:1 #F8B6C0\n"
"    );\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #B60019, stop:1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"}\n"
"\n"
"QPushButton#pushButton:checked {\n"
"    background-color: qlineargradient(\n"
"        x1:0, y1:0, x2:0, y2:1,\n"
"        stop:0 #FF8DA0, stop:1 #FF7A8D\n"
"    );\n"
"    color: "
                        "#2E3440;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    border: 1px solid #ddd;\n"
"    border-radius: 8px;\n"
"    background-color: #fafafa;\n"
"    margin-top: 12px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 5px;\n"
"    color: #444;\n"
"    font-weight: 600;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"QFrame#frame_10, #frame_8{\n"
"   background-color: #FAF9F6;\n"
"    border: 2px solid blue;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#drawing_options_group_frame,#frame_7,#camera_angles_group_frame{\n"
"	background-color:transparent;\n"
"	border: 2px solid #B60019;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLabel#label_21,#label_20{\n"
"	font-family: 'Bell MT';\n"
"	font-size: 22px;\n"
"	background-color: transparent;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QRadioButton{\n"
"	color: #B60019;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLCDNumber {\n"
"    background-color: #ffffff;        /* White back"
                        "ground */\n"
"    color: #B60019;                   /* Main red digit color */\n"
"    border: 2px solid #B60019;        /* Red border */\n"
"    border-radius: 6px;               /* Slightly rounded corners */\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QLabel#status_label_center,#status_label_front{\n"
"	background-color:transparent;\n"
"}\n"
"\n"
"QLabel#slogan_about_us {\n"
"  font-family: 'Bell MT';\n"
"	font-size: 40px;\n"
"	font-weight: 500;\n"
"    padding: 6px 12px;\n"
"	color: #B60019;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLabel#label_83 {\n"
"	background-color: transparent;	\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #ffffff;  /* Pure white */\n"
"    color: #2c2c2c;             /* Dark gray text for readability */\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    font-size: 14px;\n"
"    border: 1px solid #ccc;     /* Light gray border */\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    selection-background-color: #cce4ff;  /* Light blue selection */\n"
"    selection"
                        "-color: #000000;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid #3399ff;  /* Blue border on focus */\n"
"}\n"
"\n"
"/* Scrollbar styling for light mode */\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #f5f5f5;  /* Light gray background */\n"
"    width: 10px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #B60019;\n"
"    min-height: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QLabel#label_40{\n"
"	border: 1px solid #B60019; /* Slightly darker border */\n"
"	font-family: 'Segoe UI';\n"
"	font-size: 14px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton#Back_to_Home_button_from_about_us {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #D91A30, stop"
                        ": 1 #B60019\n"
"    );\n"
"    color: white;\n"
"    border: 1px solid #9E0014;\n"
"    border-radius: 5px;\n"
"    padding: 8px 14px;\n"
"    font-size: 18px;\n"
"    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);\n"
"}\n"
"\n"
"QPushButton#Back_to_Home_button_from_about_us:hover {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #E53950, stop: 1 #CC1028\n"
"    );\n"
"}\n"
"\n"
"QPushButton#Back_to_Home_button_from_about_us:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #B60019, stop: 1 #900012\n"
"    );\n"
"    border: 1px solid #78000F;\n"
"    padding-top: 9px; padding-bottom: 7px; /* Subtle press-down effect */\n"
"    box-shadow: inset 0px 2px 4px rgba(0, 0, 0, 0.2); /* Inner shadow */\n"
"}\n"
"\n"
"QPushButton#Back_to_Home_button_from_about_us:checked {\n"
"   background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #FF8DA0, stop: 1 #FF7A8D\n"
"    "
                        ");\n"
"    color: #2E3440;\n"
"}\n"
"\n"
"QFrame #frame_5{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLabel#slogan1 {\n"
"    font-family: 'Bell MT';\n"
"    font-size: 30px;\n"
"    font-style: italic;           /* \u2190 Correct way to italicize */\n"
"    padding: 6px 12px;\n"
"    color: #B60019;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QLabel#slogan2 {\n"
"    font-family: 'Bell MT';\n"
"    font-size: 35px;\n"
"    font-weight: bold;           /* \u2190 Correct way to italicize */\n"
"    padding: 6px 12px;\n"
"    color: #B60019;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QLabel#slogan3 {\n"
"    font-family: 'Bell MT';\n"
"    font-size: 35px;\n"
"    font-weight: bold;           \n"
"    padding: 6px 12px;\n"
"    color: #B60019;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QLabel#small_intro {\n"
"    font-family: 'Cambria';\n"
"    font-size: 20px;        /* \u2190 Correct way to italicize */\n"
"    padding: 6px 12px;\n"
"    color: black;\n"
"    backgroun"
                        "d-color: transparent;\n"
"}\n"
"\n"
"QLabel#label_22 {\n"
"	font-family: 'Bell MT';\n"
"    font-size: 18px;\n"
"    font-weight: bold;           /* \u2190 Correct way to italicize */\n"
"    padding: 6px 12px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton#view_button_advanced_analytics_heatmap {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #fff5f5, stop: 1 #ffe6e6\n"
"    );\n"
"    color: #990000;  /* Dark red text for contrast */\n"
"    border: 1px solid #ffcccc;\n"
"    border-radius: 10px;\n"
"    font-size: 14px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"    /* Qt doesn't support box-shadow, but this is left in case your platform does */\n"
"    /* box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); */\n"
"}\n"
"\n"
"QPushButton#view_button_advanced_analytics_heatmap:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffe6e6, stop: 1 #ffd6d6\n"
"    );\n"
"    bor"
                        "der: 1px solid #ffb3b3;\n"
"}\n"
"\n"
"QPushButton#view_button_advanced_analytics_heatmap:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffd6d6, stop: 1 #ffb3b3\n"
"    );\n"
"    border: 1px solid #e68a8a;\n"
"    /* Simulated \"pressed\" effect */\n"
"}\n"
"\n"
"QPushButton#view_button_advanced_analytics_heatmap:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffebeb, stop: 1 #ffc2c2\n"
"    );\n"
"    color: #800000;\n"
"    border: 1px solid #e69999;\n"
"}\n"
"\n"
"QPushButton#view_button_ai_analytics_heatmap {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #fff5f5, stop: 1 #ffe6e6\n"
"    );\n"
"    color: #990000;  /* Dark red text for contrast */\n"
"    border: 1px solid #ffcccc;\n"
"    border-radius: 10px;\n"
"    font-size: 14px;\n"
"    padding: 8px 16px;\n"
"    font-weight: 600;\n"
"    /* Qt doesn't support box"
                        "-shadow, but this is left in case your platform does */\n"
"    /* box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1); */\n"
"}\n"
"\n"
"QPushButton#view_button_ai_analytics_heatmap:hover {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffe6e6, stop: 1 #ffd6d6\n"
"    );\n"
"    border: 1px solid #ffb3b3;\n"
"}\n"
"\n"
"QPushButton#view_button_ai_analytics_heatmap:pressed {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffd6d6, stop: 1 #ffb3b3\n"
"    );\n"
"    border: 1px solid #e68a8a;\n"
"    /* Simulated \"pressed\" effect */\n"
"}\n"
"\n"
"QPushButton#view_button_ai_analytics_heatmap:checked {\n"
"    background-color: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 #ffebeb, stop: 1 #ffc2c2\n"
"    );\n"
"    color: #800000;\n"
"    border: 1px solid #e69999;\n"
"}\n"
"\n"
"QLabel#label_45,#ai_analytics_count_students{\n"
"	color: black;\n"
"	font-weight: bold;\n"
"}\n"
""
                        "\n"
"QLabel#label_33,#ai_analytics_count_left_arm_extending_sidewards{\n"
"	color: #ff5b79;\n"
"}\n"
"\n"
"QLabel#label_36,#ai_analytics_count_right_arm_extending_sidewards{\n"
"	color: #db4dd6;\n"
"}\n"
"\n"
"QLabel#label_37,#ai_analytics_count_facing_downwards{\n"
"	color: #34a0b2;\n"
"}\n"
"\n"
"QLabel#label_39,#ai_analytics_count_facing_forward{\n"
"	color: #f7cd61;\n"
"}\n"
"\n"
"QLabel#label_41,#ai_analytics_count_facing_left{\n"
"	color: #eee574;\n"
"}\n"
"\n"
"QLabel#label_42,#ai_analytics_count_facing_right{\n"
"	color: #caff8f;\n"
"}\n"
"\n"
"QLabel#label_44,#ai_analytics_count_standing{\n"
"	color: #ee7160;\n"
"}\n"
"\n"
"QLabel#label_43,#ai_analytics_count_sitting{\n"
"	color: #ba55d3;\n"
"}\n"
"\n"
"QLabel#label_76,#advanced_analytics_count_students{\n"
"	color: black;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QLabel#label_60,#advanced_analytics_count_left_arm_extending_sidewards{\n"
"	color: #ff6347;\n"
"}\n"
"\n"
"QLabel#label_61,#advanced_analytics_count_left_arm_neutral{\n"
"	color: #228b22;\n"
""
                        "}\n"
"\n"
"QLabel#label_62,#advanced_analytics_count_left_arm_unknown{\n"
"	color: #8a2be2;\n"
"}\n"
"\n"
"QLabel#label_53,#advanced_analytics_count_right_arm_extending_sidewards{\n"
"	color: #ff8c00;\n"
"}\n"
"\n"
"QLabel#label_63,#advanced_analytics_count_right_arm_neutral{\n"
"	color: #4682b4;\n"
"}\n"
"\n"
"QLabel#label_64,#advanced_analytics_count_right_arm_unknown{\n"
"	color: #20b2aa;\n"
"}\n"
"\n"
"QLabel#label_56,#advanced_analytics_count_facing_downwards{\n"
"	color: #ffdf00;\n"
"}\n"
"\n"
"QLabel#label_59,#advanced_analytics_count_facing_forward{\n"
"	color: #00ced1;\n"
"}\n"
"\n"
"QLabel#label_57,#advanced_analytics_count_facing_left{\n"
"	color: #ff69b4;\n"
"}\n"
"\n"
"QLabel#label_58,#advanced_analytics_count_facing_right{\n"
"	color: #ba55d3;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    background-color: #FAF9F6;\n"
"    alternate-background-color: #f2f1ed;\n"
"    border: 1px solid #B60019;\n"
"    border-radius: 8px;\n"
"    gridline-color: #B60019;  /* Visible and in theme */\n"
"    font-size: 13px"
                        ";\n"
"    color: #333333;\n"
"    selection-background-color: #B60019;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #B60019;\n"
"    color: white;\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #9e0015;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #B60019;\n"
"    border: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #FAF9F6;\n"
"    width: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: #B60019;\n"
"    min-height: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: #FAF9F6;\n"
"    height: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: #B60019;\n"
"    min-width: 20px;\n"
"    border-radius:"
                        " 5px;\n"
"}\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QLabel#label_2,#label_3{\n"
"	font-family: 'Segoe UI';\n"
"	font-size: 20px;\n"
"	color: #CC1028;\n"
"    padding: 6px 12px;\n"
"	font-weight: bold;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QLabel#label_40,#label_67{\n"
"	font-family:'Segoe UI';\n"
"	font-size:14px;\n"
" 	background-color: transparent;  /* Default background */\n"
"    color: #B60019;               /* Text color */    \n"
"	border: 1px solid #e0a800; /* Slightly darker border */\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLabel#time_elapsed_label_front{\n"
"	color: #B60019;\n"
"	font-family:'Segoe UI';\n"
"	font-size:14px;\n"
" 	background-color: transparent;\n"
"	\n"
"}\n"
"\n"
"QLabel#time_elapsed_label_center{\n"
"	color: #B60019;\n"
"	font-family:'Segoe UI';\n"
"	font-size:14px;\n"
" 	background-color: transparent;\n"
"	\n"
"}")
        self.actionTutorial_Tab = QAction(MainWindow)
        self.actionTutorial_Tab.setObjectName(u"actionTutorial_Tab")
        self.actionAbout_Us = QAction(MainWindow)
        self.actionAbout_Us.setObjectName(u"actionAbout_Us")
        self.actionCreate_Dataset_Tab = QAction(MainWindow)
        self.actionCreate_Dataset_Tab.setObjectName(u"actionCreate_Dataset_Tab")
        self.actionHome = QAction(MainWindow)
        self.actionHome.setObjectName(u"actionHome")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.actionAI_Analytics = QAction(MainWindow)
        self.actionAI_Analytics.setObjectName(u"actionAI_Analytics")
        self.actionAdvanced_Analytics = QAction(MainWindow)
        self.actionAdvanced_Analytics.setObjectName(u"actionAdvanced_Analytics")
        self.actionExport_Data = QAction(MainWindow)
        self.actionExport_Data.setObjectName(u"actionExport_Data")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionImport_Video = QAction(MainWindow)
        self.actionImport_Video.setObjectName(u"actionImport_Video")
        icon1 = QIcon()
        icon1.addFile(u":/icons/data-transfer-upload-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionImport_Video.setIcon(icon1)
        self.actionExit_Application = QAction(MainWindow)
        self.actionExit_Application.setObjectName(u"actionExit_Application")
        icon2 = QIcon()
        icon2.addFile(u":/icons/close-window-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionExit_Application.setIcon(icon2)
        self.actionAI_Analytics_Tab = QAction(MainWindow)
        self.actionAI_Analytics_Tab.setObjectName(u"actionAI_Analytics_Tab")
        icon3 = QIcon()
        icon3.addFile(u":/icons/brain-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAI_Analytics_Tab.setIcon(icon3)
        self.actionAdvanced_Analytics_2 = QAction(MainWindow)
        self.actionAdvanced_Analytics_2.setObjectName(u"actionAdvanced_Analytics_2")
        self.actionAI_Analytics_Results = QAction(MainWindow)
        self.actionAI_Analytics_Results.setObjectName(u"actionAI_Analytics_Results")
        self.actionAI_Analytics_Results.setIcon(icon3)
        self.actionAdvanced_Analytics_Results = QAction(MainWindow)
        self.actionAdvanced_Analytics_Results.setObjectName(u"actionAdvanced_Analytics_Results")
        icon4 = QIcon()
        icon4.addFile(u":/icons/analytics-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAdvanced_Analytics_Results.setIcon(icon4)
        self.actionExport_Data_Analytics_Results = QAction(MainWindow)
        self.actionExport_Data_Analytics_Results.setObjectName(u"actionExport_Data_Analytics_Results")
        icon5 = QIcon()
        icon5.addFile(u":/icons/data-transfer-download-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionExport_Data_Analytics_Results.setIcon(icon5)
        self.actionAbout_Us_Panel = QAction(MainWindow)
        self.actionAbout_Us_Panel.setObjectName(u"actionAbout_Us_Panel")
        icon6 = QIcon()
        icon6.addFile(u":/icons/info-5-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionAbout_Us_Panel.setIcon(icon6)
        self.actionTutorial = QAction(MainWindow)
        self.actionTutorial.setObjectName(u"actionTutorial")
        icon7 = QIcon()
        icon7.addFile(u":/icons/info-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionTutorial.setIcon(icon7)
        self.actionNew_Project = QAction(MainWindow)
        self.actionNew_Project.setObjectName(u"actionNew_Project")
        icon8 = QIcon()
        icon8.addFile(u":/icons/report-3-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.actionNew_Project.setIcon(icon8)
        self.actionCreate_Dataset = QAction(MainWindow)
        self.actionCreate_Dataset.setObjectName(u"actionCreate_Dataset")
        self.actionCalibrate_Camera = QAction(MainWindow)
        self.actionCalibrate_Camera.setObjectName(u"actionCalibrate_Camera")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 181, 661))
        self.frame.setFrameShape(QFrame.Shape.WinPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.ProjectName = QLabel(self.frame)
        self.ProjectName.setObjectName(u"ProjectName")
        self.ProjectName.setGeometry(QRect(20, 60, 151, 51))
        font1 = QFont()
        font1.setFamilies([u"Bell MT"])
        self.ProjectName.setFont(font1)
        self.ProjectName.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Home_button = QPushButton(self.frame)
        self.Home_button.setObjectName(u"Home_button")
        self.Home_button.setGeometry(QRect(10, 116, 161, 61))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setWeight(QFont.Medium)
        self.Home_button.setFont(font2)
        self.Home_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Home_button.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    padding-left: 10px;  \n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/home-4-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Home_button.setIcon(icon9)
        self.Home_button.setIconSize(QSize(20, 20))
        self.Home_button.setCheckable(True)
        self.Home_button.setAutoExclusive(True)
        self.Import_button = QPushButton(self.frame)
        self.Import_button.setObjectName(u"Import_button")
        self.Import_button.setEnabled(False)
        self.Import_button.setGeometry(QRect(10, 190, 161, 61))
        self.Import_button.setFont(font2)
        self.Import_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Import_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Import_button.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    padding-left: 10px;  \n"
"	line-heightL 50%\n"
"\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/low-importance-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Import_button.setIcon(icon10)
        self.Import_button.setIconSize(QSize(20, 20))
        self.Import_button.setCheckable(True)
        self.Import_button.setAutoRepeat(False)
        self.Import_button.setAutoExclusive(True)
        self.Import_button.setAutoDefault(False)
        self.Exit_button = QPushButton(self.frame)
        self.Exit_button.setObjectName(u"Exit_button")
        self.Exit_button.setGeometry(QRect(10, 590, 161, 61))
        self.Exit_button.setFont(font2)
        self.Exit_button.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    padding-left: 10px;  \n"
"	line-height: 50%\n"
"\n"
"}")
        self.Exit_button.setIcon(icon2)
        self.Exit_button.setIconSize(QSize(20, 20))
        self.Advanced_analytics_button = QPushButton(self.frame)
        self.Advanced_analytics_button.setObjectName(u"Advanced_analytics_button")
        self.Advanced_analytics_button.setEnabled(False)
        self.Advanced_analytics_button.setGeometry(QRect(10, 330, 161, 61))
        self.Advanced_analytics_button.setFont(font2)
        self.Advanced_analytics_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Advanced_analytics_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Advanced_analytics_button.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    padding-left: 10px;  \n"
"	line-height: 50%\n"
"\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/activity-feed-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Advanced_analytics_button.setIcon(icon11)
        self.Advanced_analytics_button.setIconSize(QSize(20, 20))
        self.Advanced_analytics_button.setCheckable(True)
        self.Advanced_analytics_button.setAutoExclusive(True)
        self.Tutorial_button = QPushButton(self.frame)
        self.Tutorial_button.setObjectName(u"Tutorial_button")
        self.Tutorial_button.setGeometry(QRect(10, 520, 161, 61))
        self.Tutorial_button.setFont(font2)
        self.Tutorial_button.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    padding-left: 10px;  \n"
"	line-height: 50%\n"
"\n"
"}")
        self.Tutorial_button.setIcon(icon7)
        self.Tutorial_button.setIconSize(QSize(20, 20))
        self.Export_file_button = QPushButton(self.frame)
        self.Export_file_button.setObjectName(u"Export_file_button")
        self.Export_file_button.setEnabled(False)
        self.Export_file_button.setGeometry(QRect(10, 400, 161, 61))
        self.Export_file_button.setFont(font2)
        self.Export_file_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Export_file_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Export_file_button.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    padding-left: 10px;  \n"
"	line-height: 50%\n"
"\n"
"}")
        self.Export_file_button.setIcon(icon8)
        self.Export_file_button.setIconSize(QSize(20, 20))
        self.Export_file_button.setCheckable(True)
        self.Export_file_button.setAutoExclusive(True)
        self.AI_analytics_button = QPushButton(self.frame)
        self.AI_analytics_button.setObjectName(u"AI_analytics_button")
        self.AI_analytics_button.setEnabled(False)
        self.AI_analytics_button.setGeometry(QRect(10, 260, 161, 61))
        self.AI_analytics_button.setFont(font2)
        self.AI_analytics_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.AI_analytics_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.AI_analytics_button.setStyleSheet(u"QPushButton {\n"
"    text-align: left;\n"
"    padding-left: 10px;  \n"
"	line-height: 50%\n"
"}")
        self.AI_analytics_button.setIcon(icon3)
        self.AI_analytics_button.setIconSize(QSize(20, 20))
        self.AI_analytics_button.setCheckable(True)
        self.AI_analytics_button.setAutoExclusive(True)
        self.logo = QLabel(self.frame)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(60, 0, 71, 71))
        self.logo.setPixmap(QPixmap(u":/icons/ACE Logo.png"))
        self.logo.setScaledContents(True)
        self.logo.raise_()
        self.Home_button.raise_()
        self.Import_button.raise_()
        self.Exit_button.raise_()
        self.Advanced_analytics_button.raise_()
        self.Tutorial_button.raise_()
        self.Export_file_button.raise_()
        self.AI_analytics_button.raise_()
        self.ProjectName.raise_()
        self.stackedPanels = QStackedWidget(self.centralwidget)
        self.stackedPanels.setObjectName(u"stackedPanels")
        self.stackedPanels.setGeometry(QRect(180, 0, 1151, 661))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedPanels.sizePolicy().hasHeightForWidth())
        self.stackedPanels.setSizePolicy(sizePolicy)
        self.stackedPanels.setMinimumSize(QSize(50, 0))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(False)
        self.stackedPanels.setFont(font3)
        self.stackedPanels.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"")
        self.stackedPanels.setFrameShape(QFrame.Shape.WinPanel)
        self.stackedPanels.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedPanels.setLineWidth(5)
        self.Homepage = QWidget()
        self.Homepage.setObjectName(u"Homepage")
        self.frame_5 = QFrame(self.Homepage)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, -1, 511, 91))
        self.frame_5.setFrameShape(QFrame.Shape.Box)
        self.frame_5.setFrameShadow(QFrame.Shadow.Plain)
        self.Homepage_label = QLabel(self.frame_5)
        self.Homepage_label.setObjectName(u"Homepage_label")
        self.Homepage_label.setGeometry(QRect(0, 0, 491, 91))
        font4 = QFont()
        font4.setFamilies([u"Bell MT"])
        font4.setWeight(QFont.Medium)
        self.Homepage_label.setFont(font4)
        self.slogan2 = QLabel(self.Homepage)
        self.slogan2.setObjectName(u"slogan2")
        self.slogan2.setGeometry(QRect(20, 150, 441, 41))
        font5 = QFont()
        font5.setFamilies([u"Bell MT"])
        font5.setBold(True)
        self.slogan2.setFont(font5)
        self.slogan3 = QLabel(self.Homepage)
        self.slogan3.setObjectName(u"slogan3")
        self.slogan3.setGeometry(QRect(20, 180, 441, 41))
        self.slogan3.setFont(font5)
        self.ImageDesign_Placeholder1 = QFrame(self.Homepage)
        self.ImageDesign_Placeholder1.setObjectName(u"ImageDesign_Placeholder1")
        self.ImageDesign_Placeholder1.setGeometry(QRect(490, 110, 205, 371))
        self.ImageDesign_Placeholder1.setFrameShape(QFrame.Shape.StyledPanel)
        self.ImageDesign_Placeholder1.setFrameShadow(QFrame.Shadow.Raised)
        self.label_14 = QLabel(self.ImageDesign_Placeholder1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 0, 531, 371))
        self.label_14.setPixmap(QPixmap(u":/icons/Home_page_picture.png"))
        self.label_14.setScaledContents(True)
        self.ImageDesign_Placeholder2 = QFrame(self.Homepage)
        self.ImageDesign_Placeholder2.setObjectName(u"ImageDesign_Placeholder2")
        self.ImageDesign_Placeholder2.setGeometry(QRect(710, 170, 205, 411))
        self.ImageDesign_Placeholder2.setFrameShape(QFrame.Shape.StyledPanel)
        self.ImageDesign_Placeholder2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_84 = QLabel(self.ImageDesign_Placeholder2)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(-160, 0, 581, 411))
        self.label_84.setPixmap(QPixmap(u":/icons/Home_page_picture.png"))
        self.label_84.setScaledContents(True)
        self.ImageDesign_Placeholder1_2 = QFrame(self.Homepage)
        self.ImageDesign_Placeholder1_2.setObjectName(u"ImageDesign_Placeholder1_2")
        self.ImageDesign_Placeholder1_2.setGeometry(QRect(930, 110, 205, 421))
        self.ImageDesign_Placeholder1_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.ImageDesign_Placeholder1_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_85 = QLabel(self.ImageDesign_Placeholder1_2)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(-380, 0, 601, 421))
        self.label_85.setPixmap(QPixmap(u":/icons/Home_page_picture.png"))
        self.label_85.setScaledContents(True)
        self.small_intro = QLabel(self.Homepage)
        self.small_intro.setObjectName(u"small_intro")
        self.small_intro.setGeometry(QRect(10, 200, 471, 311))
        self.small_intro.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.small_intro.setTextFormat(Qt.TextFormat.PlainText)
        self.small_intro.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.small_intro.setWordWrap(False)
        self.frame_9 = QFrame(self.Homepage)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(-10, 20, 1191, 661))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.label_86 = QLabel(self.frame_9)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(-20, 10, 631, 611))
        self.label_86.setPixmap(QPixmap(u":/icons_resource/SPARTA.png"))
        self.label_86.setScaledContents(True)
        self.label_87 = QLabel(self.frame_9)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(460, -80, 721, 731))
        self.label_87.setPixmap(QPixmap(u":/icons/LOGO TRANSPARENT.png"))
        self.label_87.setScaledContents(True)
        self.label_88 = QLabel(self.frame_9)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setGeometry(QRect(-80, -90, 721, 731))
        self.label_88.setPixmap(QPixmap(u":/icons/SPARTA.png"))
        self.label_88.setScaledContents(True)
        self.start_button = QPushButton(self.frame_9)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(180, 560, 121, 51))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        self.start_button.setFont(font6)
        self.label_22 = QLabel(self.frame_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(10, 479, 221, 31))
        self.label_22.setFont(font5)
        self.sessionName_line_edit = QLineEdit(self.frame_9)
        self.sessionName_line_edit.setObjectName(u"sessionName_line_edit")
        self.sessionName_line_edit.setGeometry(QRect(30, 510, 441, 41))
        self.slogan1 = QLabel(self.frame_9)
        self.slogan1.setObjectName(u"slogan1")
        self.slogan1.setGeometry(QRect(30, 90, 441, 41))
        font7 = QFont()
        font7.setFamilies([u"Bell MT"])
        font7.setItalic(True)
        font7.setStyleStrategy(QFont.PreferDefault)
        self.slogan1.setFont(font7)
        self.slogan1.setTextFormat(Qt.TextFormat.PlainText)
        self.slogan1.setMargin(0)
        self.label_86.raise_()
        self.label_88.raise_()
        self.label_87.raise_()
        self.start_button.raise_()
        self.label_22.raise_()
        self.sessionName_line_edit.raise_()
        self.slogan1.raise_()
        self.stackedPanels.addWidget(self.Homepage)
        self.frame_9.raise_()
        self.frame_5.raise_()
        self.slogan2.raise_()
        self.slogan3.raise_()
        self.ImageDesign_Placeholder1.raise_()
        self.ImageDesign_Placeholder2.raise_()
        self.ImageDesign_Placeholder1_2.raise_()
        self.small_intro.raise_()
        self.ImportPage = QWidget()
        self.ImportPage.setObjectName(u"ImportPage")
        self.frame_8 = QFrame(self.ImportPage)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(10, 420, 1131, 231))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.status_label_front = QLabel(self.frame_8)
        self.status_label_front.setObjectName(u"status_label_front")
        self.status_label_front.setGeometry(QRect(10, 110, 541, 20))
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setItalic(True)
        self.status_label_front.setFont(font8)
        self.status_label_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.import_video_button_front = QPushButton(self.frame_8)
        self.import_video_button_front.setObjectName(u"import_video_button_front")
        self.import_video_button_front.setGeometry(QRect(449, 40, 101, 31))
        self.import_video_button_front.setMaximumSize(QSize(140, 50))
        self.import_video_button_front.setFont(font3)
        self.import_video_button_front.setAutoFillBackground(False)
        icon12 = QIcon()
        icon12.addFile(u":/icons/search-13-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.import_video_button_front.setIcon(icon12)
        self.import_video_button_front.setIconSize(QSize(15, 17))
        self.videoDirectory_front = QLineEdit(self.frame_8)
        self.videoDirectory_front.setObjectName(u"videoDirectory_front")
        self.videoDirectory_front.setGeometry(QRect(10, 40, 431, 31))
        self.videoDirectory_front.setFont(font8)
        self.videoDirectory_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.videoDirectory_front.setReadOnly(True)
        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 10, 175, 21))
        self.label_15.setMaximumSize(QSize(211, 21))
        self.label_15.setFont(font8)
        self.importProgressBar_front = QProgressBar(self.frame_8)
        self.importProgressBar_front.setObjectName(u"importProgressBar_front")
        self.importProgressBar_front.setGeometry(QRect(30, 80, 521, 31))
        self.importProgressBar_front.setFont(font)
        self.importProgressBar_front.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #880000;\n"
"    border-radius: 6px;\n"
"    background-color: #f0f0f0;\n"
"    text-align: center;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 #cc0000, \n"
"        stop: 1 #990000\n"
"    );\n"
"    border-radius: 6px;\n"
"    margin: 1px;\n"
"}\n"
"")
        self.importProgressBar_front.setValue(0)
        self.importProgressBar_front.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.label_17 = QLabel(self.frame_8)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(580, 10, 184, 21))
        self.label_17.setMaximumSize(QSize(211, 21))
        self.label_17.setFont(font8)
        self.importProgressBar_center = QProgressBar(self.frame_8)
        self.importProgressBar_center.setObjectName(u"importProgressBar_center")
        self.importProgressBar_center.setGeometry(QRect(580, 80, 541, 31))
        self.importProgressBar_center.setFont(font)
        self.importProgressBar_center.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #880000;\n"
"    border-radius: 6px;\n"
"    background-color: #f0f0f0;\n"
"    text-align: center;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 #cc0000, \n"
"        stop: 1 #990000\n"
"    );\n"
"    border-radius: 6px;\n"
"    margin: 1px;\n"
"}\n"
"")
        self.importProgressBar_center.setValue(0)
        self.importProgressBar_center.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignTrailing)
        self.videoDirectory_center = QLineEdit(self.frame_8)
        self.videoDirectory_center.setObjectName(u"videoDirectory_center")
        self.videoDirectory_center.setGeometry(QRect(580, 40, 431, 31))
        self.videoDirectory_center.setFont(font8)
        self.videoDirectory_center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.videoDirectory_center.setReadOnly(True)
        self.status_label_center = QLabel(self.frame_8)
        self.status_label_center.setObjectName(u"status_label_center")
        self.status_label_center.setGeometry(QRect(580, 110, 541, 20))
        self.status_label_center.setFont(font8)
        self.status_label_center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.import_video_button_center = QPushButton(self.frame_8)
        self.import_video_button_center.setObjectName(u"import_video_button_center")
        self.import_video_button_center.setGeometry(QRect(1020, 40, 101, 31))
        self.import_video_button_center.setFont(font6)
        self.import_video_button_center.setIcon(icon12)
        self.import_video_button_center.setIconSize(QSize(15, 17))
        self.play_pause_button_video_preview = QPushButton(self.frame_8)
        self.play_pause_button_video_preview.setObjectName(u"play_pause_button_video_preview")
        self.play_pause_button_video_preview.setEnabled(False)
        self.play_pause_button_video_preview.setGeometry(QRect(920, 160, 201, 61))
        font9 = QFont()
        font9.setFamilies([u"Segoe UI"])
        font9.setWeight(QFont.DemiBold)
        self.play_pause_button_video_preview.setFont(font9)
        icon13 = QIcon()
        icon13.addFile(u":/icons/play-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_pause_button_video_preview.setIcon(icon13)
        self.play_pause_button_video_preview.setIconSize(QSize(17, 17))
        self.time_frame_container_import_preview = QWidget(self.frame_8)
        self.time_frame_container_import_preview.setObjectName(u"time_frame_container_import_preview")
        self.time_frame_container_import_preview.setGeometry(QRect(10, 160, 901, 61))
        self.time_frame_container_import_preview.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.label_40 = QLabel(self.frame_8)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, 130, 101, 31))
        self.label_40.setFont(font6)
        self.time_elapsed_label_front = QLabel(self.frame_8)
        self.time_elapsed_label_front.setObjectName(u"time_elapsed_label_front")
        self.time_elapsed_label_front.setGeometry(QRect(120, 130, 431, 31))
        self.time_elapsed_label_front.setFont(font6)
        self.time_elapsed_label_center = QLabel(self.frame_8)
        self.time_elapsed_label_center.setObjectName(u"time_elapsed_label_center")
        self.time_elapsed_label_center.setGeometry(QRect(684, 130, 431, 31))
        self.time_elapsed_label_center.setFont(font6)
        self.label_67 = QLabel(self.frame_8)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setGeometry(QRect(580, 130, 101, 31))
        self.label_67.setFont(font6)
        self.import_video_button_front.raise_()
        self.videoDirectory_front.raise_()
        self.label_15.raise_()
        self.importProgressBar_front.raise_()
        self.label_17.raise_()
        self.importProgressBar_center.raise_()
        self.videoDirectory_center.raise_()
        self.status_label_center.raise_()
        self.import_video_button_center.raise_()
        self.play_pause_button_video_preview.raise_()
        self.status_label_front.raise_()
        self.time_frame_container_import_preview.raise_()
        self.label_40.raise_()
        self.time_elapsed_label_front.raise_()
        self.time_elapsed_label_center.raise_()
        self.label_67.raise_()
        self.label_18 = QLabel(self.ImportPage)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(970, 10, 31, 17))
        self.label_18.setMaximumSize(QSize(31, 21))
        self.label_18.setFont(font6)
        self.timeLCD = QLCDNumber(self.ImportPage)
        self.timeLCD.setObjectName(u"timeLCD")
        self.timeLCD.setGeometry(QRect(970, 30, 161, 41))
        self.timeLCD.setMaximumSize(QSize(161, 41))
        self.timeLCD.setFont(font6)
        self.timeLCD.setAutoFillBackground(False)
        self.timeLCD.setFrameShadow(QFrame.Shadow.Sunken)
        self.timeLCD.setLineWidth(1)
        self.timeLCD.setMidLineWidth(0)
        self.timeLCD.setDigitCount(8)
        self.timeLCD.setSegmentStyle(QLCDNumber.SegmentStyle.Filled)
        self.label_30 = QLabel(self.ImportPage)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 90, 151, 21))
        self.label_30.setMaximumSize(QSize(191, 21))
        self.label_30.setFont(font6)
        self.label_30.setAutoFillBackground(False)
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_29 = QLabel(self.ImportPage)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(580, 90, 151, 21))
        self.label_29.setMaximumSize(QSize(191, 21))
        self.label_29.setFont(font6)
        self.label_29.setAutoFillBackground(False)
        self.label_29.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.day_label = QLabel(self.ImportPage)
        self.day_label.setObjectName(u"day_label")
        self.day_label.setGeometry(QRect(760, 30, 201, 41))
        font10 = QFont()
        font10.setFamilies([u"Segoe UI"])
        font10.setItalic(False)
        self.day_label.setFont(font10)
        self.label_23 = QLabel(self.ImportPage)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(560, 10, 91, 21))
        self.label_24 = QLabel(self.ImportPage)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(760, 10, 31, 21))
        self.session_name_label = QLabel(self.ImportPage)
        self.session_name_label.setObjectName(u"session_name_label")
        self.session_name_label.setGeometry(QRect(560, 30, 191, 41))
        self.session_name_label.setFont(font10)
        self.label_27 = QLabel(self.ImportPage)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 0, 561, 91))
        self.label_27.setFont(font4)
        self.video_preview_label_front = QLabel(self.ImportPage)
        self.video_preview_label_front.setObjectName(u"video_preview_label_front")
        self.video_preview_label_front.setGeometry(QRect(10, 90, 561, 321))
        self.video_preview_label_front.setFont(font8)
        self.video_preview_label_front.setFrameShape(QFrame.Shape.WinPanel)
        self.video_preview_label_front.setFrameShadow(QFrame.Shadow.Raised)
        self.video_preview_label_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video_preview_label_center = QLabel(self.ImportPage)
        self.video_preview_label_center.setObjectName(u"video_preview_label_center")
        self.video_preview_label_center.setGeometry(QRect(580, 90, 561, 321))
        self.video_preview_label_center.setFont(font8)
        self.video_preview_label_center.setFrameShape(QFrame.Shape.WinPanel)
        self.video_preview_label_center.setFrameShadow(QFrame.Shadow.Raised)
        self.video_preview_label_center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.front_preview_video_keypoints_check_box = QCheckBox(self.ImportPage)
        self.front_preview_video_keypoints_check_box.setObjectName(u"front_preview_video_keypoints_check_box")
        self.front_preview_video_keypoints_check_box.setGeometry(QRect(180, 92, 81, 20))
        self.front_preview_video_bounding_box_check_box = QCheckBox(self.ImportPage)
        self.front_preview_video_bounding_box_check_box.setObjectName(u"front_preview_video_bounding_box_check_box")
        self.front_preview_video_bounding_box_check_box.setGeometry(QRect(290, 92, 121, 20))
        self.center_preview_video_bounding_box_check_box = QCheckBox(self.ImportPage)
        self.center_preview_video_bounding_box_check_box.setObjectName(u"center_preview_video_bounding_box_check_box")
        self.center_preview_video_bounding_box_check_box.setGeometry(QRect(860, 92, 121, 20))
        self.center_preview_video_keypoints_check_box = QCheckBox(self.ImportPage)
        self.center_preview_video_keypoints_check_box.setObjectName(u"center_preview_video_keypoints_check_box")
        self.center_preview_video_keypoints_check_box.setGeometry(QRect(750, 92, 81, 20))
        self.front_preview_video_dark_mode_check_box = QCheckBox(self.ImportPage)
        self.front_preview_video_dark_mode_check_box.setObjectName(u"front_preview_video_dark_mode_check_box")
        self.front_preview_video_dark_mode_check_box.setEnabled(True)
        self.front_preview_video_dark_mode_check_box.setGeometry(QRect(430, 92, 121, 20))
        self.center_preview_video_dark_mode_check_box = QCheckBox(self.ImportPage)
        self.center_preview_video_dark_mode_check_box.setObjectName(u"center_preview_video_dark_mode_check_box")
        self.center_preview_video_dark_mode_check_box.setEnabled(True)
        self.center_preview_video_dark_mode_check_box.setGeometry(QRect(1000, 92, 121, 20))
        self.stackedPanels.addWidget(self.ImportPage)
        self.frame_8.raise_()
        self.label_18.raise_()
        self.timeLCD.raise_()
        self.day_label.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.session_name_label.raise_()
        self.label_27.raise_()
        self.video_preview_label_front.raise_()
        self.video_preview_label_center.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.front_preview_video_keypoints_check_box.raise_()
        self.front_preview_video_bounding_box_check_box.raise_()
        self.center_preview_video_bounding_box_check_box.raise_()
        self.center_preview_video_keypoints_check_box.raise_()
        self.front_preview_video_dark_mode_check_box.raise_()
        self.center_preview_video_dark_mode_check_box.raise_()
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stacked_panels_ai_analytics = QStackedWidget(self.page_4)
        self.stacked_panels_ai_analytics.setObjectName(u"stacked_panels_ai_analytics")
        self.stacked_panels_ai_analytics.setGeometry(QRect(0, 60, 1151, 601))
        self.stacked_panels_ai_analytics.setStyleSheet(u"")
        self.stacked_panels_ai_analytics.setFrameShape(QFrame.Shape.NoFrame)
        self.stacked_panels_ai_analytics.setFrameShadow(QFrame.Shadow.Raised)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.video_preview_label_ai_analytics_center = QLabel(self.page_12)
        self.video_preview_label_ai_analytics_center.setObjectName(u"video_preview_label_ai_analytics_center")
        self.video_preview_label_ai_analytics_center.setGeometry(QRect(643, 10, 501, 231))
        self.video_preview_label_ai_analytics_center.setFont(font8)
        self.video_preview_label_ai_analytics_center.setFrameShape(QFrame.Shape.WinPanel)
        self.video_preview_label_ai_analytics_center.setFrameShadow(QFrame.Shadow.Raised)
        self.video_preview_label_ai_analytics_center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.video_preview_label_ai_analytics_front = QLabel(self.page_12)
        self.video_preview_label_ai_analytics_front.setObjectName(u"video_preview_label_ai_analytics_front")
        self.video_preview_label_ai_analytics_front.setGeometry(QRect(643, 250, 501, 291))
        self.video_preview_label_ai_analytics_front.setFont(font8)
        self.video_preview_label_ai_analytics_front.setFrameShape(QFrame.Shape.WinPanel)
        self.video_preview_label_ai_analytics_front.setFrameShadow(QFrame.Shadow.Raised)
        self.video_preview_label_ai_analytics_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.visualization_stackedpanels_3 = QStackedWidget(self.page_12)
        self.visualization_stackedpanels_3.setObjectName(u"visualization_stackedpanels_3")
        self.visualization_stackedpanels_3.setGeometry(QRect(10, 10, 621, 531))
        self.visualization_stackedpanels_3.setFrameShape(QFrame.Shape.WinPanel)
        self.visualization_stackedpanels_3.setLineWidth(1)
        self.Heatmap_3 = QWidget()
        self.Heatmap_3.setObjectName(u"Heatmap_3")
        self.heatmap_ai_analytics_label = QLabel(self.Heatmap_3)
        self.heatmap_ai_analytics_label.setObjectName(u"heatmap_ai_analytics_label")
        self.heatmap_ai_analytics_label.setGeometry(QRect(10, 70, 601, 451))
        self.heatmap_ai_analytics_label.setFont(font8)
        self.heatmap_ai_analytics_label.setFrameShape(QFrame.Shape.WinPanel)
        self.heatmap_ai_analytics_label.setFrameShadow(QFrame.Shadow.Raised)
        self.heatmap_ai_analytics_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_15 = QFrame(self.Heatmap_3)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(10, 3, 601, 61))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.heatmap_actions_ai_analytics_combo_box = QComboBox(self.frame_15)
        self.heatmap_actions_ai_analytics_combo_box.addItem("")
        self.heatmap_actions_ai_analytics_combo_box.addItem("")
        self.heatmap_actions_ai_analytics_combo_box.addItem("")
        self.heatmap_actions_ai_analytics_combo_box.addItem("")
        self.heatmap_actions_ai_analytics_combo_box.addItem("")
        self.heatmap_actions_ai_analytics_combo_box.addItem("")
        self.heatmap_actions_ai_analytics_combo_box.addItem("")
        self.heatmap_actions_ai_analytics_combo_box.addItem("")
        self.heatmap_actions_ai_analytics_combo_box.addItem("")
        self.heatmap_actions_ai_analytics_combo_box.setObjectName(u"heatmap_actions_ai_analytics_combo_box")
        self.heatmap_actions_ai_analytics_combo_box.setGeometry(QRect(10, 10, 471, 41))
        self.heatmap_actions_ai_analytics_combo_box.setFont(font10)
        self.heatmap_actions_ai_analytics_combo_box.setMaxVisibleItems(12)
        self.view_button_ai_analytics_heatmap = QPushButton(self.frame_15)
        self.view_button_ai_analytics_heatmap.setObjectName(u"view_button_ai_analytics_heatmap")
        self.view_button_ai_analytics_heatmap.setGeometry(QRect(490, 10, 101, 41))
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        font11.setWeight(QFont.DemiBold)
        font11.setItalic(False)
        self.view_button_ai_analytics_heatmap.setFont(font11)
        icon14 = QIcon()
        icon14.addFile(u":/icons_resource/search-13-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.view_button_ai_analytics_heatmap.setIcon(icon14)
        self.view_button_ai_analytics_heatmap.setIconSize(QSize(20, 25))
        self.visualization_stackedpanels_3.addWidget(self.Heatmap_3)
        self.Visualization1_3 = QWidget()
        self.Visualization1_3.setObjectName(u"Visualization1_3")
        self.visualization1_label_3 = QLabel(self.Visualization1_3)
        self.visualization1_label_3.setObjectName(u"visualization1_label_3")
        self.visualization1_label_3.setGeometry(QRect(20, 29, 600, 361))
        self.visualization1_label_3.setFont(font8)
        self.visualization1_label_3.setFrameShape(QFrame.Shape.WinPanel)
        self.visualization1_label_3.setFrameShadow(QFrame.Shadow.Raised)
        self.visualization1_label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.visualization_stackedpanels_3.addWidget(self.Visualization1_3)
        self.Visualization2_3 = QWidget()
        self.Visualization2_3.setObjectName(u"Visualization2_3")
        self.heatmap_present_label_6 = QLabel(self.Visualization2_3)
        self.heatmap_present_label_6.setObjectName(u"heatmap_present_label_6")
        self.heatmap_present_label_6.setGeometry(QRect(9, 10, 621, 351))
        self.heatmap_present_label_6.setFont(font8)
        self.heatmap_present_label_6.setFrameShape(QFrame.Shape.WinPanel)
        self.heatmap_present_label_6.setFrameShadow(QFrame.Shadow.Raised)
        self.heatmap_present_label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.visualization_stackedpanels_3.addWidget(self.Visualization2_3)
        self.play_pause_button_ai_analytics_heatmap = QPushButton(self.page_12)
        self.play_pause_button_ai_analytics_heatmap.setObjectName(u"play_pause_button_ai_analytics_heatmap")
        self.play_pause_button_ai_analytics_heatmap.setGeometry(QRect(950, 550, 191, 41))
        self.play_pause_button_ai_analytics_heatmap.setFont(font9)
        self.play_pause_button_ai_analytics_heatmap.setIcon(icon13)
        self.CenterPlacement_label_3 = QLabel(self.page_12)
        self.CenterPlacement_label_3.setObjectName(u"CenterPlacement_label_3")
        self.CenterPlacement_label_3.setGeometry(QRect(643, 10, 161, 31))
        self.CenterPlacement_label_3.setFont(font8)
        self.CenterPlacement_label_3.setAutoFillBackground(False)
        self.CenterPlacement_label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.keypoints_check_box_ai_analytics_center = QCheckBox(self.page_12)
        self.keypoints_check_box_ai_analytics_center.setObjectName(u"keypoints_check_box_ai_analytics_center")
        self.keypoints_check_box_ai_analytics_center.setGeometry(QRect(926, 10, 111, 31))
        self.keypoints_check_box_ai_analytics_center.setAutoFillBackground(False)
        self.bounding_box_check_box_ai_analytics_center = QCheckBox(self.page_12)
        self.bounding_box_check_box_ai_analytics_center.setObjectName(u"bounding_box_check_box_ai_analytics_center")
        self.bounding_box_check_box_ai_analytics_center.setGeometry(QRect(811, 10, 111, 31))
        self.bounding_box_check_box_ai_analytics_center.setAutoFillBackground(False)
        self.bounding_box_check_box_ai_analytics_center.setChecked(False)
        self.bounding_box_check_box_ai_analytics_front = QCheckBox(self.page_12)
        self.bounding_box_check_box_ai_analytics_front.setObjectName(u"bounding_box_check_box_ai_analytics_front")
        self.bounding_box_check_box_ai_analytics_front.setGeometry(QRect(812, 250, 111, 31))
        self.bounding_box_check_box_ai_analytics_front.setAutoFillBackground(False)
        self.bounding_box_check_box_ai_analytics_front.setChecked(False)
        self.keypoints_check_box_ai_analytics_front = QCheckBox(self.page_12)
        self.keypoints_check_box_ai_analytics_front.setObjectName(u"keypoints_check_box_ai_analytics_front")
        self.keypoints_check_box_ai_analytics_front.setGeometry(QRect(927, 250, 121, 31))
        self.keypoints_check_box_ai_analytics_front.setAutoFillBackground(False)
        self.FrontPlacement_label_3 = QLabel(self.page_12)
        self.FrontPlacement_label_3.setObjectName(u"FrontPlacement_label_3")
        self.FrontPlacement_label_3.setGeometry(QRect(644, 250, 161, 31))
        self.FrontPlacement_label_3.setFont(font8)
        self.FrontPlacement_label_3.setAutoFillBackground(False)
        self.FrontPlacement_label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_frame_container_heatmap_ai_analytics = QWidget(self.page_12)
        self.time_frame_container_heatmap_ai_analytics.setObjectName(u"time_frame_container_heatmap_ai_analytics")
        self.time_frame_container_heatmap_ai_analytics.setGeometry(QRect(10, 550, 821, 41))
        self.time_frame_container_heatmap_ai_analytics.setStyleSheet(u"")
        self.dark_mode_check_box_ai_analytics_center = QCheckBox(self.page_12)
        self.dark_mode_check_box_ai_analytics_center.setObjectName(u"dark_mode_check_box_ai_analytics_center")
        self.dark_mode_check_box_ai_analytics_center.setGeometry(QRect(1049, 10, 141, 31))
        self.dark_mode_check_box_ai_analytics_center.setAutoFillBackground(False)
        self.dark_mode_check_box_ai_analytics_front = QCheckBox(self.page_12)
        self.dark_mode_check_box_ai_analytics_front.setObjectName(u"dark_mode_check_box_ai_analytics_front")
        self.dark_mode_check_box_ai_analytics_front.setGeometry(QRect(1050, 250, 141, 31))
        self.dark_mode_check_box_ai_analytics_front.setAutoFillBackground(False)
        self.identify_suspicious_check_box_heatmap_ai_analytics = QCheckBox(self.page_12)
        self.identify_suspicious_check_box_heatmap_ai_analytics.setObjectName(u"identify_suspicious_check_box_heatmap_ai_analytics")
        self.identify_suspicious_check_box_heatmap_ai_analytics.setGeometry(QRect(840, 550, 101, 41))
        self.identify_suspicious_check_box_heatmap_ai_analytics.setFont(font)
        self.stacked_panels_ai_analytics.addWidget(self.page_12)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.ai_analytics_preview_front = QLabel(self.page_9)
        self.ai_analytics_preview_front.setObjectName(u"ai_analytics_preview_front")
        self.ai_analytics_preview_front.setGeometry(QRect(10, 10, 464, 261))
        font12 = QFont()
        font12.setFamilies([u"Segoe UI"])
        font12.setBold(False)
        font12.setItalic(True)
        self.ai_analytics_preview_front.setFont(font12)
        self.ai_analytics_preview_front.setFrameShape(QFrame.Shape.WinPanel)
        self.ai_analytics_preview_front.setFrameShadow(QFrame.Shadow.Raised)
        self.ai_analytics_preview_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_frame_container_line_graph_ai_analytics = QWidget(self.page_9)
        self.time_frame_container_line_graph_ai_analytics.setObjectName(u"time_frame_container_line_graph_ai_analytics")
        self.time_frame_container_line_graph_ai_analytics.setGeometry(QRect(0, 270, 471, 51))
        self.time_frame_container_line_graph_ai_analytics.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.ai_analytics_preview_center = QLabel(self.page_9)
        self.ai_analytics_preview_center.setObjectName(u"ai_analytics_preview_center")
        self.ai_analytics_preview_center.setGeometry(QRect(480, 10, 464, 261))
        self.ai_analytics_preview_center.setFont(font8)
        self.ai_analytics_preview_center.setFrameShape(QFrame.Shape.WinPanel)
        self.ai_analytics_preview_center.setFrameShadow(QFrame.Shadow.Raised)
        self.ai_analytics_preview_center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.play_pause_button__ai_analytics_line_graph = QPushButton(self.page_9)
        self.play_pause_button__ai_analytics_line_graph.setObjectName(u"play_pause_button__ai_analytics_line_graph")
        self.play_pause_button__ai_analytics_line_graph.setGeometry(QRect(950, 280, 191, 41))
        self.play_pause_button__ai_analytics_line_graph.setFont(font9)
        self.play_pause_button__ai_analytics_line_graph.setIcon(icon13)
        self.ai_analytics_line_graph_combo_box = MultiSelectComboBox(self.page_9)
        self.ai_analytics_line_graph_combo_box.setObjectName(u"ai_analytics_line_graph_combo_box")
        self.ai_analytics_line_graph_combo_box.setGeometry(QRect(480, 280, 351, 41))
        self.ai_analytics_line_graph_combo_box.setFont(font6)
        self.ai_analytics_line_chart = QGraphicsView(self.page_9)
        self.ai_analytics_line_chart.setObjectName(u"ai_analytics_line_chart")
        self.ai_analytics_line_chart.setGeometry(QRect(10, 330, 1131, 261))
        self.label_33 = QLabel(self.page_9)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(950, 70, 171, 41))
        self.label_33.setFont(font6)
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_36 = QLabel(self.page_9)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(950, 110, 161, 41))
        self.label_36.setFont(font6)
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_37 = QLabel(self.page_9)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(950, 150, 111, 21))
        self.label_37.setFont(font6)
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_39 = QLabel(self.page_9)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(950, 165, 111, 31))
        self.label_39.setFont(font6)
        self.label_39.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_41 = QLabel(self.page_9)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(950, 190, 111, 21))
        self.label_41.setFont(font6)
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_42 = QLabel(self.page_9)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(950, 210, 111, 21))
        self.label_42.setFont(font6)
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_43 = QLabel(self.page_9)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(950, 230, 111, 21))
        self.label_43.setFont(font6)
        self.label_43.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_44 = QLabel(self.page_9)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(950, 250, 111, 21))
        self.label_44.setFont(font6)
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.front_preview_video_bounding_box_ai_analytics_line_graph_check_box = QCheckBox(self.page_9)
        self.front_preview_video_bounding_box_ai_analytics_line_graph_check_box.setObjectName(u"front_preview_video_bounding_box_ai_analytics_line_graph_check_box")
        self.front_preview_video_bounding_box_ai_analytics_line_graph_check_box.setGeometry(QRect(290, 10, 121, 20))
        self.front_preview_video_keypoints_ai_analytics_line_graph_check_box = QCheckBox(self.page_9)
        self.front_preview_video_keypoints_ai_analytics_line_graph_check_box.setObjectName(u"front_preview_video_keypoints_ai_analytics_line_graph_check_box")
        self.front_preview_video_keypoints_ai_analytics_line_graph_check_box.setGeometry(QRect(180, 10, 81, 20))
        self.label_31 = QLabel(self.page_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(10, 10, 161, 21))
        self.label_31.setMaximumSize(QSize(191, 21))
        self.label_31.setFont(font6)
        self.label_31.setAutoFillBackground(False)
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_32 = QLabel(self.page_9)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(480, 10, 161, 21))
        self.label_32.setMaximumSize(QSize(191, 21))
        self.label_32.setFont(font6)
        self.label_32.setAutoFillBackground(False)
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.center_preview_video_bounding_box_ai_analytics_line_graph_check_box = QCheckBox(self.page_9)
        self.center_preview_video_bounding_box_ai_analytics_line_graph_check_box.setObjectName(u"center_preview_video_bounding_box_ai_analytics_line_graph_check_box")
        self.center_preview_video_bounding_box_ai_analytics_line_graph_check_box.setGeometry(QRect(760, 10, 121, 20))
        self.center_preview_video_keypoints_ai_analytics_line_graph_check_box = QCheckBox(self.page_9)
        self.center_preview_video_keypoints_ai_analytics_line_graph_check_box.setObjectName(u"center_preview_video_keypoints_ai_analytics_line_graph_check_box")
        self.center_preview_video_keypoints_ai_analytics_line_graph_check_box.setGeometry(QRect(650, 10, 81, 20))
        self.ai_analytics_count_standing = QLabel(self.page_9)
        self.ai_analytics_count_standing.setObjectName(u"ai_analytics_count_standing")
        self.ai_analytics_count_standing.setGeometry(QRect(1100, 250, 31, 21))
        self.ai_analytics_count_standing.setFont(font6)
        self.ai_analytics_count_standing.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.ai_analytics_count_sitting = QLabel(self.page_9)
        self.ai_analytics_count_sitting.setObjectName(u"ai_analytics_count_sitting")
        self.ai_analytics_count_sitting.setGeometry(QRect(1100, 230, 31, 21))
        self.ai_analytics_count_sitting.setFont(font6)
        self.ai_analytics_count_sitting.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.ai_analytics_count_facing_right = QLabel(self.page_9)
        self.ai_analytics_count_facing_right.setObjectName(u"ai_analytics_count_facing_right")
        self.ai_analytics_count_facing_right.setGeometry(QRect(1100, 210, 31, 21))
        self.ai_analytics_count_facing_right.setFont(font6)
        self.ai_analytics_count_facing_right.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.ai_analytics_count_facing_left = QLabel(self.page_9)
        self.ai_analytics_count_facing_left.setObjectName(u"ai_analytics_count_facing_left")
        self.ai_analytics_count_facing_left.setGeometry(QRect(1100, 190, 31, 21))
        self.ai_analytics_count_facing_left.setFont(font6)
        self.ai_analytics_count_facing_left.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.ai_analytics_count_facing_forward = QLabel(self.page_9)
        self.ai_analytics_count_facing_forward.setObjectName(u"ai_analytics_count_facing_forward")
        self.ai_analytics_count_facing_forward.setGeometry(QRect(1100, 170, 31, 21))
        self.ai_analytics_count_facing_forward.setFont(font6)
        self.ai_analytics_count_facing_forward.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.ai_analytics_count_facing_downwards = QLabel(self.page_9)
        self.ai_analytics_count_facing_downwards.setObjectName(u"ai_analytics_count_facing_downwards")
        self.ai_analytics_count_facing_downwards.setGeometry(QRect(1100, 150, 31, 21))
        self.ai_analytics_count_facing_downwards.setFont(font6)
        self.ai_analytics_count_facing_downwards.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.ai_analytics_count_right_arm_extending_sidewards = QLabel(self.page_9)
        self.ai_analytics_count_right_arm_extending_sidewards.setObjectName(u"ai_analytics_count_right_arm_extending_sidewards")
        self.ai_analytics_count_right_arm_extending_sidewards.setGeometry(QRect(1100, 110, 31, 41))
        self.ai_analytics_count_right_arm_extending_sidewards.setFont(font6)
        self.ai_analytics_count_right_arm_extending_sidewards.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.ai_analytics_count_left_arm_extending_sidewards = QLabel(self.page_9)
        self.ai_analytics_count_left_arm_extending_sidewards.setObjectName(u"ai_analytics_count_left_arm_extending_sidewards")
        self.ai_analytics_count_left_arm_extending_sidewards.setGeometry(QRect(1100, 80, 31, 31))
        self.ai_analytics_count_left_arm_extending_sidewards.setFont(font6)
        self.ai_analytics_count_left_arm_extending_sidewards.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_45 = QLabel(self.page_9)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(950, 50, 161, 21))
        self.label_45.setFont(font)
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.ai_analytics_count_students = QLabel(self.page_9)
        self.ai_analytics_count_students.setObjectName(u"ai_analytics_count_students")
        self.ai_analytics_count_students.setGeometry(QRect(1100, 51, 31, 20))
        self.ai_analytics_count_students.setFont(font)
        self.ai_analytics_count_students.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_55 = QLabel(self.page_9)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(950, 10, 181, 41))
        font13 = QFont()
        font13.setFamilies([u"Segoe UI"])
        font13.setBold(True)
        font13.setItalic(True)
        self.label_55.setFont(font13)
        self.label_55.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.identify_suspicious_check_box_line_graph_ai_analytics = QCheckBox(self.page_9)
        self.identify_suspicious_check_box_line_graph_ai_analytics.setObjectName(u"identify_suspicious_check_box_line_graph_ai_analytics")
        self.identify_suspicious_check_box_line_graph_ai_analytics.setGeometry(QRect(840, 280, 101, 41))
        self.identify_suspicious_check_box_line_graph_ai_analytics.setFont(font)
        self.stacked_panels_ai_analytics.addWidget(self.page_9)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.time_frame_container_table_event_logs_ai_analytics = QWidget(self.page_11)
        self.time_frame_container_table_event_logs_ai_analytics.setObjectName(u"time_frame_container_table_event_logs_ai_analytics")
        self.time_frame_container_table_event_logs_ai_analytics.setGeometry(QRect(0, 280, 1141, 51))
        self.time_frame_container_table_event_logs_ai_analytics.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.play_pause_button_ai_analytics_table_event_logs = QPushButton(self.page_11)
        self.play_pause_button_ai_analytics_table_event_logs.setObjectName(u"play_pause_button_ai_analytics_table_event_logs")
        self.play_pause_button_ai_analytics_table_event_logs.setGeometry(QRect(950, 230, 191, 41))
        self.play_pause_button_ai_analytics_table_event_logs.setFont(font9)
        self.play_pause_button_ai_analytics_table_event_logs.setIcon(icon13)
        self.ai_analytics_table_event_logs_preview_front = QLabel(self.page_11)
        self.ai_analytics_table_event_logs_preview_front.setObjectName(u"ai_analytics_table_event_logs_preview_front")
        self.ai_analytics_table_event_logs_preview_front.setGeometry(QRect(10, 10, 464, 261))
        self.ai_analytics_table_event_logs_preview_front.setFont(font12)
        self.ai_analytics_table_event_logs_preview_front.setStyleSheet(u"")
        self.ai_analytics_table_event_logs_preview_front.setFrameShape(QFrame.Shape.WinPanel)
        self.ai_analytics_table_event_logs_preview_front.setFrameShadow(QFrame.Shadow.Raised)
        self.ai_analytics_table_event_logs_preview_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ai_analytics_table_event_logs_preview_center = QLabel(self.page_11)
        self.ai_analytics_table_event_logs_preview_center.setObjectName(u"ai_analytics_table_event_logs_preview_center")
        self.ai_analytics_table_event_logs_preview_center.setGeometry(QRect(480, 10, 464, 261))
        self.ai_analytics_table_event_logs_preview_center.setFont(font8)
        self.ai_analytics_table_event_logs_preview_center.setFrameShape(QFrame.Shape.WinPanel)
        self.ai_analytics_table_event_logs_preview_center.setFrameShadow(QFrame.Shadow.Raised)
        self.ai_analytics_table_event_logs_preview_center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ai_analytics_event_logs_table_1 = QTableWidget(self.page_11)
        if (self.ai_analytics_event_logs_table_1.columnCount() < 3):
            self.ai_analytics_event_logs_table_1.setColumnCount(3)
        self.ai_analytics_event_logs_table_1.setObjectName(u"ai_analytics_event_logs_table_1")
        self.ai_analytics_event_logs_table_1.setGeometry(QRect(10, 330, 371, 261))
        self.ai_analytics_event_logs_table_1.setLineWidth(1)
        self.ai_analytics_event_logs_table_1.setMidLineWidth(0)
        self.ai_analytics_event_logs_table_1.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.ai_analytics_event_logs_table_1.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.ai_analytics_event_logs_table_1.setGridStyle(Qt.PenStyle.NoPen)
        self.ai_analytics_event_logs_table_1.setSortingEnabled(True)
        self.ai_analytics_event_logs_table_1.setColumnCount(3)
        self.ai_analytics_event_logs_table_1.verticalHeader().setVisible(False)
        self.ai_analytics_event_logs_table_2 = QTableWidget(self.page_11)
        if (self.ai_analytics_event_logs_table_2.columnCount() < 3):
            self.ai_analytics_event_logs_table_2.setColumnCount(3)
        self.ai_analytics_event_logs_table_2.setObjectName(u"ai_analytics_event_logs_table_2")
        self.ai_analytics_event_logs_table_2.setGeometry(QRect(390, 330, 371, 261))
        self.ai_analytics_event_logs_table_2.setLineWidth(1)
        self.ai_analytics_event_logs_table_2.setMidLineWidth(0)
        self.ai_analytics_event_logs_table_2.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.ai_analytics_event_logs_table_2.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.ai_analytics_event_logs_table_2.setGridStyle(Qt.PenStyle.NoPen)
        self.ai_analytics_event_logs_table_2.setSortingEnabled(True)
        self.ai_analytics_event_logs_table_2.setColumnCount(3)
        self.ai_analytics_event_logs_table_2.horizontalHeader().setVisible(True)
        self.ai_analytics_event_logs_table_2.horizontalHeader().setCascadingSectionResizes(False)
        self.ai_analytics_event_logs_table_2.verticalHeader().setVisible(False)
        self.ai_analytics_event_logs_table_3 = QTableWidget(self.page_11)
        if (self.ai_analytics_event_logs_table_3.columnCount() < 3):
            self.ai_analytics_event_logs_table_3.setColumnCount(3)
        self.ai_analytics_event_logs_table_3.setObjectName(u"ai_analytics_event_logs_table_3")
        self.ai_analytics_event_logs_table_3.setGeometry(QRect(770, 330, 371, 261))
        self.ai_analytics_event_logs_table_3.setLineWidth(1)
        self.ai_analytics_event_logs_table_3.setMidLineWidth(0)
        self.ai_analytics_event_logs_table_3.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.ai_analytics_event_logs_table_3.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.ai_analytics_event_logs_table_3.setGridStyle(Qt.PenStyle.NoPen)
        self.ai_analytics_event_logs_table_3.setSortingEnabled(True)
        self.ai_analytics_event_logs_table_3.setColumnCount(3)
        self.ai_analytics_event_logs_table_3.verticalHeader().setVisible(False)
        self.TimeLabel = QLabel(self.page_11)
        self.TimeLabel.setObjectName(u"TimeLabel")
        self.TimeLabel.setGeometry(QRect(950, 130, 191, 41))
        self.TimeLabel.setFont(font6)
        self.TimeLabel_2 = QLabel(self.page_11)
        self.TimeLabel_2.setObjectName(u"TimeLabel_2")
        self.TimeLabel_2.setGeometry(QRect(950, 90, 81, 31))
        self.TimeLabel_2.setFont(font6)
        self.center_preview_video_keypoints_ai_analytics_event_logs_check_box = QCheckBox(self.page_11)
        self.center_preview_video_keypoints_ai_analytics_event_logs_check_box.setObjectName(u"center_preview_video_keypoints_ai_analytics_event_logs_check_box")
        self.center_preview_video_keypoints_ai_analytics_event_logs_check_box.setGeometry(QRect(670, 12, 81, 20))
        self.center_preview_video_bounding_box_ai_analytics_event_logs_check_box = QCheckBox(self.page_11)
        self.center_preview_video_bounding_box_ai_analytics_event_logs_check_box.setObjectName(u"center_preview_video_bounding_box_ai_analytics_event_logs_check_box")
        self.center_preview_video_bounding_box_ai_analytics_event_logs_check_box.setGeometry(QRect(780, 12, 121, 20))
        self.label_46 = QLabel(self.page_11)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(480, 10, 161, 21))
        self.label_46.setMaximumSize(QSize(191, 21))
        self.label_46.setFont(font6)
        self.label_46.setAutoFillBackground(False)
        self.label_46.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.front_preview_video_keypoints_ai_analytics_event_logs_check_box = QCheckBox(self.page_11)
        self.front_preview_video_keypoints_ai_analytics_event_logs_check_box.setObjectName(u"front_preview_video_keypoints_ai_analytics_event_logs_check_box")
        self.front_preview_video_keypoints_ai_analytics_event_logs_check_box.setGeometry(QRect(200, 12, 81, 20))
        self.front_preview_video_bounding_box_ai_analytics_event_logs_check_box = QCheckBox(self.page_11)
        self.front_preview_video_bounding_box_ai_analytics_event_logs_check_box.setObjectName(u"front_preview_video_bounding_box_ai_analytics_event_logs_check_box")
        self.front_preview_video_bounding_box_ai_analytics_event_logs_check_box.setGeometry(QRect(310, 12, 121, 20))
        self.label_47 = QLabel(self.page_11)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(10, 10, 161, 21))
        self.label_47.setMaximumSize(QSize(191, 21))
        self.label_47.setFont(font6)
        self.label_47.setAutoFillBackground(False)
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.stacked_panels_ai_analytics.addWidget(self.page_11)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.ai_analytics_event_summary_table = QTableWidget(self.page_8)
        if (self.ai_analytics_event_summary_table.columnCount() < 2):
            self.ai_analytics_event_summary_table.setColumnCount(2)
        font14 = QFont()
        font14.setFamilies([u"Bell MT"])
        font14.setPointSize(14)
        font14.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font14);
        self.ai_analytics_event_summary_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font15 = QFont()
        font15.setFamilies([u"Bell MT"])
        font15.setPointSize(16)
        font15.setBold(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font15);
        self.ai_analytics_event_summary_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.ai_analytics_event_summary_table.rowCount() < 5):
            self.ai_analytics_event_summary_table.setRowCount(5)
        self.ai_analytics_event_summary_table.setObjectName(u"ai_analytics_event_summary_table")
        self.ai_analytics_event_summary_table.setGeometry(QRect(10, 330, 1131, 261))
        self.ai_analytics_event_summary_table.setFont(font6)
        self.ai_analytics_event_summary_table.setLineWidth(1)
        self.ai_analytics_event_summary_table.setMidLineWidth(0)
        self.ai_analytics_event_summary_table.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.ai_analytics_event_summary_table.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.ai_analytics_event_summary_table.setGridStyle(Qt.PenStyle.NoPen)
        self.ai_analytics_event_summary_table.setSortingEnabled(True)
        self.ai_analytics_event_summary_table.setRowCount(5)
        self.ai_analytics_event_summary_table.setColumnCount(2)
        self.ai_analytics_event_summary_table.verticalHeader().setVisible(False)
        self.front_preview_video_bounding_box_ai_analytics_event_summary_check_box = QCheckBox(self.page_8)
        self.front_preview_video_bounding_box_ai_analytics_event_summary_check_box.setObjectName(u"front_preview_video_bounding_box_ai_analytics_event_summary_check_box")
        self.front_preview_video_bounding_box_ai_analytics_event_summary_check_box.setGeometry(QRect(310, 12, 221, 20))
        self.front_preview_video_bounding_box_ai_analytics_event_summary_check_box.setAutoFillBackground(False)
        self.center_preview_video_keypoints_ai_analytics_event_summary_check_box = QCheckBox(self.page_8)
        self.center_preview_video_keypoints_ai_analytics_event_summary_check_box.setObjectName(u"center_preview_video_keypoints_ai_analytics_event_summary_check_box")
        self.center_preview_video_keypoints_ai_analytics_event_summary_check_box.setGeometry(QRect(670, 12, 91, 20))
        self.center_preview_video_keypoints_ai_analytics_event_summary_check_box.setAutoFillBackground(False)
        self.ai_analytics_chunk_summary_preview_front = QLabel(self.page_8)
        self.ai_analytics_chunk_summary_preview_front.setObjectName(u"ai_analytics_chunk_summary_preview_front")
        self.ai_analytics_chunk_summary_preview_front.setGeometry(QRect(10, 10, 461, 260))
        self.ai_analytics_chunk_summary_preview_front.setFont(font12)
        self.ai_analytics_chunk_summary_preview_front.setStyleSheet(u"")
        self.ai_analytics_chunk_summary_preview_front.setFrameShape(QFrame.Shape.WinPanel)
        self.ai_analytics_chunk_summary_preview_front.setFrameShadow(QFrame.Shadow.Raised)
        self.ai_analytics_chunk_summary_preview_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_70 = QLabel(self.page_8)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(10, 10, 161, 21))
        self.label_70.setMaximumSize(QSize(191, 21))
        self.label_70.setFont(font6)
        self.label_70.setAutoFillBackground(False)
        self.label_70.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.center_preview_video_bounding_box_ai_analytics_event_summary_check_box = QCheckBox(self.page_8)
        self.center_preview_video_bounding_box_ai_analytics_event_summary_check_box.setObjectName(u"center_preview_video_bounding_box_ai_analytics_event_summary_check_box")
        self.center_preview_video_bounding_box_ai_analytics_event_summary_check_box.setGeometry(QRect(780, 12, 201, 20))
        self.center_preview_video_bounding_box_ai_analytics_event_summary_check_box.setAutoFillBackground(False)
        self.ai_analytics_chunk_summary_preview_center = QLabel(self.page_8)
        self.ai_analytics_chunk_summary_preview_center.setObjectName(u"ai_analytics_chunk_summary_preview_center")
        self.ai_analytics_chunk_summary_preview_center.setGeometry(QRect(475, 10, 461, 260))
        self.ai_analytics_chunk_summary_preview_center.setFont(font8)
        self.ai_analytics_chunk_summary_preview_center.setFrameShape(QFrame.Shape.WinPanel)
        self.ai_analytics_chunk_summary_preview_center.setFrameShadow(QFrame.Shadow.Raised)
        self.ai_analytics_chunk_summary_preview_center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_71 = QLabel(self.page_8)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(480, 10, 161, 21))
        self.label_71.setMaximumSize(QSize(191, 21))
        self.label_71.setFont(font6)
        self.label_71.setAutoFillBackground(False)
        self.label_71.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.front_preview_video_keypoints_ai_analytics_event_summary_check_box = QCheckBox(self.page_8)
        self.front_preview_video_keypoints_ai_analytics_event_summary_check_box.setObjectName(u"front_preview_video_keypoints_ai_analytics_event_summary_check_box")
        self.front_preview_video_keypoints_ai_analytics_event_summary_check_box.setGeometry(QRect(200, 12, 81, 20))
        self.front_preview_video_keypoints_ai_analytics_event_summary_check_box.setAutoFillBackground(False)
        self.ai_analytics_event_summary_play_pause_button = QPushButton(self.page_8)
        self.ai_analytics_event_summary_play_pause_button.setObjectName(u"ai_analytics_event_summary_play_pause_button")
        self.ai_analytics_event_summary_play_pause_button.setGeometry(QRect(940, 215, 201, 51))
        self.ai_analytics_event_summary_play_pause_button.setFont(font9)
        self.ai_analytics_event_summary_play_pause_button.setIcon(icon13)
        self.ai_analytics_interval_slider_minutes = QSlider(self.page_8)
        self.ai_analytics_interval_slider_minutes.setObjectName(u"ai_analytics_interval_slider_minutes")
        self.ai_analytics_interval_slider_minutes.setGeometry(QRect(940, 60, 201, 31))
        self.ai_analytics_interval_slider_minutes.setMaximum(5)
        self.ai_analytics_interval_slider_minutes.setOrientation(Qt.Orientation.Horizontal)
        self.label_72 = QLabel(self.page_8)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(940, 10, 201, 31))
        font16 = QFont()
        font16.setFamilies([u"Segoe UI"])
        font16.setBold(True)
        font16.setItalic(True)
        font16.setKerning(False)
        self.label_72.setFont(font16)
        self.label_72.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_73 = QLabel(self.page_8)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(940, 90, 131, 31))
        self.label_73.setFont(font6)
        self.ai_analytics_interval_slider_seconds = QSlider(self.page_8)
        self.ai_analytics_interval_slider_seconds.setObjectName(u"ai_analytics_interval_slider_seconds")
        self.ai_analytics_interval_slider_seconds.setGeometry(QRect(940, 110, 201, 31))
        self.ai_analytics_interval_slider_seconds.setMaximum(60)
        self.ai_analytics_interval_slider_seconds.setValue(2)
        self.ai_analytics_interval_slider_seconds.setOrientation(Qt.Orientation.Horizontal)
        self.label_74 = QLabel(self.page_8)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setGeometry(QRect(940, 140, 181, 41))
        self.label_74.setFont(font6)
        self.label_75 = QLabel(self.page_8)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(940, 40, 131, 31))
        self.label_75.setFont(font6)
        self.interval_time_label = QLabel(self.page_8)
        self.interval_time_label.setObjectName(u"interval_time_label")
        self.interval_time_label.setGeometry(QRect(940, 170, 201, 31))
        self.interval_time_label.setFont(font)
        self.interval_time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_frame_container_table_event_summary_ai_analytics = QWidget(self.page_8)
        self.time_frame_container_table_event_summary_ai_analytics.setObjectName(u"time_frame_container_table_event_summary_ai_analytics")
        self.time_frame_container_table_event_summary_ai_analytics.setGeometry(QRect(0, 270, 1141, 61))
        self.time_frame_container_table_event_summary_ai_analytics.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.stacked_panels_ai_analytics.addWidget(self.page_8)
        self.ai_analytics_event_summary_table.raise_()
        self.ai_analytics_chunk_summary_preview_front.raise_()
        self.label_70.raise_()
        self.ai_analytics_chunk_summary_preview_center.raise_()
        self.label_71.raise_()
        self.front_preview_video_keypoints_ai_analytics_event_summary_check_box.raise_()
        self.ai_analytics_event_summary_play_pause_button.raise_()
        self.center_preview_video_bounding_box_ai_analytics_event_summary_check_box.raise_()
        self.center_preview_video_keypoints_ai_analytics_event_summary_check_box.raise_()
        self.front_preview_video_bounding_box_ai_analytics_event_summary_check_box.raise_()
        self.ai_analytics_interval_slider_minutes.raise_()
        self.label_72.raise_()
        self.label_73.raise_()
        self.ai_analytics_interval_slider_seconds.raise_()
        self.label_74.raise_()
        self.label_75.raise_()
        self.interval_time_label.raise_()
        self.time_frame_container_table_event_summary_ai_analytics.raise_()
        self.ai_analytics_label = QLabel(self.page_4)
        self.ai_analytics_label.setObjectName(u"ai_analytics_label")
        self.ai_analytics_label.setGeometry(QRect(10, 0, 821, 61))
        self.ai_analytics_label.setFont(font4)
        self.ai_analytics_visualization_combo_box = QComboBox(self.page_4)
        self.ai_analytics_visualization_combo_box.addItem("")
        self.ai_analytics_visualization_combo_box.addItem("")
        self.ai_analytics_visualization_combo_box.addItem("")
        self.ai_analytics_visualization_combo_box.addItem("")
        self.ai_analytics_visualization_combo_box.setObjectName(u"ai_analytics_visualization_combo_box")
        self.ai_analytics_visualization_combo_box.setGeometry(QRect(910, 10, 221, 51))
        self.ai_analytics_visualization_combo_box.setFont(font6)
        self.ai_analytics_visualization_combo_box.setIconSize(QSize(22, 22))
        self.label_35 = QLabel(self.page_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(790, 10, 121, 51))
        self.label_35.setFont(font6)
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.stackedPanels.addWidget(self.page_4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stacked_advanced_analytics = QStackedWidget(self.page)
        self.stacked_advanced_analytics.setObjectName(u"stacked_advanced_analytics")
        self.stacked_advanced_analytics.setGeometry(QRect(0, 60, 1151, 601))
        self.stacked_advanced_analytics.setFrameShape(QFrame.Shape.NoFrame)
        self.stacked_advanced_analytics.setFrameShadow(QFrame.Shadow.Raised)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.advanced_analytics_heatmap_preview_center = QLabel(self.page_3)
        self.advanced_analytics_heatmap_preview_center.setObjectName(u"advanced_analytics_heatmap_preview_center")
        self.advanced_analytics_heatmap_preview_center.setGeometry(QRect(640, 10, 501, 231))
        self.advanced_analytics_heatmap_preview_center.setFont(font8)
        self.advanced_analytics_heatmap_preview_center.setFrameShape(QFrame.Shape.WinPanel)
        self.advanced_analytics_heatmap_preview_center.setFrameShadow(QFrame.Shadow.Raised)
        self.advanced_analytics_heatmap_preview_center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.advanced_analytics_heatmap_preview_front = QLabel(self.page_3)
        self.advanced_analytics_heatmap_preview_front.setObjectName(u"advanced_analytics_heatmap_preview_front")
        self.advanced_analytics_heatmap_preview_front.setGeometry(QRect(640, 250, 501, 291))
        self.advanced_analytics_heatmap_preview_front.setFont(font8)
        self.advanced_analytics_heatmap_preview_front.setFrameShape(QFrame.Shape.WinPanel)
        self.advanced_analytics_heatmap_preview_front.setFrameShadow(QFrame.Shadow.Raised)
        self.advanced_analytics_heatmap_preview_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.visualization_stackedpanels_2 = QStackedWidget(self.page_3)
        self.visualization_stackedpanels_2.setObjectName(u"visualization_stackedpanels_2")
        self.visualization_stackedpanels_2.setGeometry(QRect(10, 10, 621, 531))
        self.visualization_stackedpanels_2.setFrameShape(QFrame.Shape.WinPanel)
        self.visualization_stackedpanels_2.setLineWidth(1)
        self.Heatmap_2 = QWidget()
        self.Heatmap_2.setObjectName(u"Heatmap_2")
        self.frame_14 = QFrame(self.Heatmap_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(10, 3, 601, 61))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.heatmap_actions_advanced_analytics_combo_box = QComboBox(self.frame_14)
        self.heatmap_actions_advanced_analytics_combo_box.addItem("")
        self.heatmap_actions_advanced_analytics_combo_box.addItem("")
        self.heatmap_actions_advanced_analytics_combo_box.addItem("")
        self.heatmap_actions_advanced_analytics_combo_box.addItem("")
        self.heatmap_actions_advanced_analytics_combo_box.addItem("")
        self.heatmap_actions_advanced_analytics_combo_box.addItem("")
        self.heatmap_actions_advanced_analytics_combo_box.addItem("")
        self.heatmap_actions_advanced_analytics_combo_box.addItem("")
        self.heatmap_actions_advanced_analytics_combo_box.addItem("")
        self.heatmap_actions_advanced_analytics_combo_box.addItem("")
        self.heatmap_actions_advanced_analytics_combo_box.addItem("")
        self.heatmap_actions_advanced_analytics_combo_box.setObjectName(u"heatmap_actions_advanced_analytics_combo_box")
        self.heatmap_actions_advanced_analytics_combo_box.setGeometry(QRect(10, 10, 471, 41))
        self.heatmap_actions_advanced_analytics_combo_box.setFont(font6)
        self.heatmap_actions_advanced_analytics_combo_box.setMaxVisibleItems(12)
        self.view_button_advanced_analytics_heatmap = QPushButton(self.frame_14)
        self.view_button_advanced_analytics_heatmap.setObjectName(u"view_button_advanced_analytics_heatmap")
        self.view_button_advanced_analytics_heatmap.setGeometry(QRect(486, 10, 101, 41))
        self.view_button_advanced_analytics_heatmap.setFont(font11)
        self.view_button_advanced_analytics_heatmap.setIcon(icon14)
        self.view_button_advanced_analytics_heatmap.setIconSize(QSize(20, 25))
        self.heatmap_advanced_analytics_label = QLabel(self.Heatmap_2)
        self.heatmap_advanced_analytics_label.setObjectName(u"heatmap_advanced_analytics_label")
        self.heatmap_advanced_analytics_label.setGeometry(QRect(10, 70, 601, 451))
        self.heatmap_advanced_analytics_label.setFont(font8)
        self.heatmap_advanced_analytics_label.setFrameShape(QFrame.Shape.WinPanel)
        self.heatmap_advanced_analytics_label.setFrameShadow(QFrame.Shadow.Raised)
        self.heatmap_advanced_analytics_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.visualization_stackedpanels_2.addWidget(self.Heatmap_2)
        self.Visualization1_2 = QWidget()
        self.Visualization1_2.setObjectName(u"Visualization1_2")
        self.visualization1_label_2 = QLabel(self.Visualization1_2)
        self.visualization1_label_2.setObjectName(u"visualization1_label_2")
        self.visualization1_label_2.setGeometry(QRect(30, 50, 600, 361))
        self.visualization1_label_2.setFont(font8)
        self.visualization1_label_2.setFrameShape(QFrame.Shape.WinPanel)
        self.visualization1_label_2.setFrameShadow(QFrame.Shadow.Raised)
        self.visualization1_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.visualization_stackedpanels_2.addWidget(self.Visualization1_2)
        self.Visualization2_2 = QWidget()
        self.Visualization2_2.setObjectName(u"Visualization2_2")
        self.heatmap_present_label_4 = QLabel(self.Visualization2_2)
        self.heatmap_present_label_4.setObjectName(u"heatmap_present_label_4")
        self.heatmap_present_label_4.setGeometry(QRect(20, 70, 621, 351))
        self.heatmap_present_label_4.setFont(font8)
        self.heatmap_present_label_4.setFrameShape(QFrame.Shape.WinPanel)
        self.heatmap_present_label_4.setFrameShadow(QFrame.Shadow.Raised)
        self.heatmap_present_label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.visualization_stackedpanels_2.addWidget(self.Visualization2_2)
        self.time_frame_container_heatmap_advanced_analytics = QWidget(self.page_3)
        self.time_frame_container_heatmap_advanced_analytics.setObjectName(u"time_frame_container_heatmap_advanced_analytics")
        self.time_frame_container_heatmap_advanced_analytics.setGeometry(QRect(10, 550, 831, 41))
        self.time_frame_container_heatmap_advanced_analytics.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.CenterPlacement_label_2 = QLabel(self.page_3)
        self.CenterPlacement_label_2.setObjectName(u"CenterPlacement_label_2")
        self.CenterPlacement_label_2.setGeometry(QRect(640, 10, 161, 31))
        self.CenterPlacement_label_2.setFont(font8)
        self.CenterPlacement_label_2.setAutoFillBackground(False)
        self.CenterPlacement_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.FrontPlacement_label_2 = QLabel(self.page_3)
        self.FrontPlacement_label_2.setObjectName(u"FrontPlacement_label_2")
        self.FrontPlacement_label_2.setGeometry(QRect(640, 250, 161, 31))
        self.FrontPlacement_label_2.setFont(font8)
        self.FrontPlacement_label_2.setAutoFillBackground(False)
        self.FrontPlacement_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.play_pause_button_advanced_analytics_heatmap = QPushButton(self.page_3)
        self.play_pause_button_advanced_analytics_heatmap.setObjectName(u"play_pause_button_advanced_analytics_heatmap")
        self.play_pause_button_advanced_analytics_heatmap.setGeometry(QRect(960, 550, 181, 41))
        self.play_pause_button_advanced_analytics_heatmap.setFont(font9)
        self.play_pause_button_advanced_analytics_heatmap.setIcon(icon13)
        self.dark_mode_check_box_advanced_analytics_center = QCheckBox(self.page_3)
        self.dark_mode_check_box_advanced_analytics_center.setObjectName(u"dark_mode_check_box_advanced_analytics_center")
        self.dark_mode_check_box_advanced_analytics_center.setGeometry(QRect(1049, 10, 141, 31))
        self.dark_mode_check_box_advanced_analytics_center.setAutoFillBackground(False)
        self.keypoints_check_box_advanced_analytics_center = QCheckBox(self.page_3)
        self.keypoints_check_box_advanced_analytics_center.setObjectName(u"keypoints_check_box_advanced_analytics_center")
        self.keypoints_check_box_advanced_analytics_center.setGeometry(QRect(926, 10, 121, 31))
        self.keypoints_check_box_advanced_analytics_center.setAutoFillBackground(False)
        self.bounding_box_check_box_advanced_analytics_center = QCheckBox(self.page_3)
        self.bounding_box_check_box_advanced_analytics_center.setObjectName(u"bounding_box_check_box_advanced_analytics_center")
        self.bounding_box_check_box_advanced_analytics_center.setGeometry(QRect(811, 10, 111, 31))
        self.bounding_box_check_box_advanced_analytics_center.setAutoFillBackground(False)
        self.bounding_box_check_box_advanced_analytics_center.setChecked(False)
        self.bounding_box_check_box_advanced_analytics_front = QCheckBox(self.page_3)
        self.bounding_box_check_box_advanced_analytics_front.setObjectName(u"bounding_box_check_box_advanced_analytics_front")
        self.bounding_box_check_box_advanced_analytics_front.setGeometry(QRect(811, 250, 111, 31))
        self.bounding_box_check_box_advanced_analytics_front.setAutoFillBackground(False)
        self.bounding_box_check_box_advanced_analytics_front.setChecked(False)
        self.dark_mode_check_box_advanced_analytics_front = QCheckBox(self.page_3)
        self.dark_mode_check_box_advanced_analytics_front.setObjectName(u"dark_mode_check_box_advanced_analytics_front")
        self.dark_mode_check_box_advanced_analytics_front.setGeometry(QRect(1049, 250, 141, 31))
        self.dark_mode_check_box_advanced_analytics_front.setAutoFillBackground(False)
        self.keypoints_check_box_advanced_analytics_front = QCheckBox(self.page_3)
        self.keypoints_check_box_advanced_analytics_front.setObjectName(u"keypoints_check_box_advanced_analytics_front")
        self.keypoints_check_box_advanced_analytics_front.setGeometry(QRect(926, 250, 121, 31))
        self.keypoints_check_box_advanced_analytics_front.setAutoFillBackground(False)
        self.identify_suspicious_check_box_heatmap_advanced_analytics = QCheckBox(self.page_3)
        self.identify_suspicious_check_box_heatmap_advanced_analytics.setObjectName(u"identify_suspicious_check_box_heatmap_advanced_analytics")
        self.identify_suspicious_check_box_heatmap_advanced_analytics.setGeometry(QRect(850, 550, 101, 41))
        self.identify_suspicious_check_box_heatmap_advanced_analytics.setFont(font)
        self.stacked_advanced_analytics.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.time_frame_container_line_graph_advanced_analytics = QWidget(self.page_2)
        self.time_frame_container_line_graph_advanced_analytics.setObjectName(u"time_frame_container_line_graph_advanced_analytics")
        self.time_frame_container_line_graph_advanced_analytics.setGeometry(QRect(0, 270, 471, 51))
        self.time_frame_container_line_graph_advanced_analytics.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.advanced_analytics_actions_combo_box = MultiSelectComboBox(self.page_2)
        self.advanced_analytics_actions_combo_box.setObjectName(u"advanced_analytics_actions_combo_box")
        self.advanced_analytics_actions_combo_box.setGeometry(QRect(480, 280, 351, 41))
        self.advanced_analytics_actions_combo_box.setFont(font6)
        self.adv_analytics_preview_line_graph_front = QLabel(self.page_2)
        self.adv_analytics_preview_line_graph_front.setObjectName(u"adv_analytics_preview_line_graph_front")
        self.adv_analytics_preview_line_graph_front.setGeometry(QRect(10, 10, 464, 261))
        self.adv_analytics_preview_line_graph_front.setFont(font12)
        self.adv_analytics_preview_line_graph_front.setFrameShape(QFrame.Shape.WinPanel)
        self.adv_analytics_preview_line_graph_front.setFrameShadow(QFrame.Shadow.Raised)
        self.adv_analytics_preview_line_graph_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adv_analytics_preview_line_graph_center = QLabel(self.page_2)
        self.adv_analytics_preview_line_graph_center.setObjectName(u"adv_analytics_preview_line_graph_center")
        self.adv_analytics_preview_line_graph_center.setGeometry(QRect(480, 10, 464, 261))
        self.adv_analytics_preview_line_graph_center.setFont(font8)
        self.adv_analytics_preview_line_graph_center.setFrameShape(QFrame.Shape.WinPanel)
        self.adv_analytics_preview_line_graph_center.setFrameShadow(QFrame.Shadow.Raised)
        self.adv_analytics_preview_line_graph_center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.play_pause_button_advanced_analytics_line_graph = QPushButton(self.page_2)
        self.play_pause_button_advanced_analytics_line_graph.setObjectName(u"play_pause_button_advanced_analytics_line_graph")
        self.play_pause_button_advanced_analytics_line_graph.setGeometry(QRect(950, 280, 191, 41))
        self.play_pause_button_advanced_analytics_line_graph.setFont(font9)
        self.play_pause_button_advanced_analytics_line_graph.setIcon(icon13)
        self.advanced_analytics_line_chart = QGraphicsView(self.page_2)
        self.advanced_analytics_line_chart.setObjectName(u"advanced_analytics_line_chart")
        self.advanced_analytics_line_chart.setGeometry(QRect(10, 330, 1131, 261))
        self.label_60 = QLabel(self.page_2)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(950, 30, 111, 41))
        self.label_60.setFont(font6)
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_57 = QLabel(self.page_2)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(950, 219, 111, 31))
        self.label_57.setFont(font6)
        self.label_57.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_59 = QLabel(self.page_2)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(950, 205, 111, 21))
        self.label_59.setFont(font6)
        self.label_59.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_58 = QLabel(self.page_2)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(950, 240, 111, 31))
        self.label_58.setFont(font6)
        self.label_58.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_56 = QLabel(self.page_2)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(950, 185, 111, 21))
        self.label_56.setFont(font6)
        self.label_56.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_53 = QLabel(self.page_2)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(950, 110, 131, 31))
        self.label_53.setFont(font6)
        self.label_53.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_61 = QLabel(self.page_2)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(950, 70, 111, 16))
        self.label_61.setFont(font6)
        self.label_61.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_62 = QLabel(self.page_2)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(950, 90, 111, 16))
        self.label_62.setFont(font6)
        self.label_62.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_63 = QLabel(self.page_2)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(950, 145, 111, 21))
        self.label_63.setFont(font6)
        self.label_63.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_64 = QLabel(self.page_2)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(950, 165, 121, 21))
        self.label_64.setFont(font6)
        self.label_64.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.front_preview_video_bounding_box_advanced_analytics_line_chart_check_box = QCheckBox(self.page_2)
        self.front_preview_video_bounding_box_advanced_analytics_line_chart_check_box.setObjectName(u"front_preview_video_bounding_box_advanced_analytics_line_chart_check_box")
        self.front_preview_video_bounding_box_advanced_analytics_line_chart_check_box.setGeometry(QRect(280, 10, 121, 20))
        self.label_48 = QLabel(self.page_2)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(480, 10, 161, 21))
        self.label_48.setMaximumSize(QSize(191, 21))
        self.label_48.setFont(font6)
        self.label_48.setAutoFillBackground(False)
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.center_preview_video_bounding_box_advanced_analytics_line_chart_check_box = QCheckBox(self.page_2)
        self.center_preview_video_bounding_box_advanced_analytics_line_chart_check_box.setObjectName(u"center_preview_video_bounding_box_advanced_analytics_line_chart_check_box")
        self.center_preview_video_bounding_box_advanced_analytics_line_chart_check_box.setGeometry(QRect(750, 10, 121, 20))
        self.label_49 = QLabel(self.page_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(10, 10, 161, 21))
        self.label_49.setMaximumSize(QSize(191, 21))
        self.label_49.setFont(font6)
        self.label_49.setAutoFillBackground(False)
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.center_preview_video_keypoints_advanced_analytics_line_chart_check_box = QCheckBox(self.page_2)
        self.center_preview_video_keypoints_advanced_analytics_line_chart_check_box.setObjectName(u"center_preview_video_keypoints_advanced_analytics_line_chart_check_box")
        self.center_preview_video_keypoints_advanced_analytics_line_chart_check_box.setGeometry(QRect(650, 10, 91, 20))
        self.front_preview_video_keypoints_advanced_analytics_line_chart_check_box = QCheckBox(self.page_2)
        self.front_preview_video_keypoints_advanced_analytics_line_chart_check_box.setObjectName(u"front_preview_video_keypoints_advanced_analytics_line_chart_check_box")
        self.front_preview_video_keypoints_advanced_analytics_line_chart_check_box.setGeometry(QRect(180, 10, 81, 20))
        self.advanced_analytics_count_facing_left = QLabel(self.page_2)
        self.advanced_analytics_count_facing_left.setObjectName(u"advanced_analytics_count_facing_left")
        self.advanced_analytics_count_facing_left.setGeometry(QRect(1100, 220, 31, 31))
        self.advanced_analytics_count_facing_left.setFont(font6)
        self.advanced_analytics_count_facing_left.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.advanced_analytics_count_left_arm_extending_sidewards = QLabel(self.page_2)
        self.advanced_analytics_count_left_arm_extending_sidewards.setObjectName(u"advanced_analytics_count_left_arm_extending_sidewards")
        self.advanced_analytics_count_left_arm_extending_sidewards.setGeometry(QRect(1100, 40, 31, 31))
        self.advanced_analytics_count_left_arm_extending_sidewards.setFont(font6)
        self.advanced_analytics_count_left_arm_extending_sidewards.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.advanced_analytics_count_facing_right = QLabel(self.page_2)
        self.advanced_analytics_count_facing_right.setObjectName(u"advanced_analytics_count_facing_right")
        self.advanced_analytics_count_facing_right.setGeometry(QRect(1100, 240, 31, 31))
        self.advanced_analytics_count_facing_right.setFont(font6)
        self.advanced_analytics_count_facing_right.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.advanced_analytics_count_right_arm_extending_sidewards = QLabel(self.page_2)
        self.advanced_analytics_count_right_arm_extending_sidewards.setObjectName(u"advanced_analytics_count_right_arm_extending_sidewards")
        self.advanced_analytics_count_right_arm_extending_sidewards.setGeometry(QRect(1100, 110, 31, 31))
        self.advanced_analytics_count_right_arm_extending_sidewards.setFont(font6)
        self.advanced_analytics_count_right_arm_extending_sidewards.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.advanced_analytics_count_facing_forward = QLabel(self.page_2)
        self.advanced_analytics_count_facing_forward.setObjectName(u"advanced_analytics_count_facing_forward")
        self.advanced_analytics_count_facing_forward.setGeometry(QRect(1100, 200, 31, 31))
        self.advanced_analytics_count_facing_forward.setFont(font6)
        self.advanced_analytics_count_facing_forward.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.advanced_analytics_count_facing_downwards = QLabel(self.page_2)
        self.advanced_analytics_count_facing_downwards.setObjectName(u"advanced_analytics_count_facing_downwards")
        self.advanced_analytics_count_facing_downwards.setGeometry(QRect(1100, 180, 31, 31))
        self.advanced_analytics_count_facing_downwards.setFont(font6)
        self.advanced_analytics_count_facing_downwards.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_76 = QLabel(self.page_2)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(950, 10, 141, 21))
        self.label_76.setFont(font)
        self.label_76.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.advanced_analytics_count_students = QLabel(self.page_2)
        self.advanced_analytics_count_students.setObjectName(u"advanced_analytics_count_students")
        self.advanced_analytics_count_students.setGeometry(QRect(1100, 10, 31, 21))
        self.advanced_analytics_count_students.setFont(font)
        self.advanced_analytics_count_students.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.advanced_analytics_count_right_arm_unknown = QLabel(self.page_2)
        self.advanced_analytics_count_right_arm_unknown.setObjectName(u"advanced_analytics_count_right_arm_unknown")
        self.advanced_analytics_count_right_arm_unknown.setGeometry(QRect(1100, 160, 31, 31))
        self.advanced_analytics_count_right_arm_unknown.setFont(font6)
        self.advanced_analytics_count_right_arm_unknown.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.advanced_analytics_count_right_arm_neutral = QLabel(self.page_2)
        self.advanced_analytics_count_right_arm_neutral.setObjectName(u"advanced_analytics_count_right_arm_neutral")
        self.advanced_analytics_count_right_arm_neutral.setGeometry(QRect(1100, 140, 31, 31))
        self.advanced_analytics_count_right_arm_neutral.setFont(font6)
        self.advanced_analytics_count_right_arm_neutral.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.advanced_analytics_count_left_arm_unknown = QLabel(self.page_2)
        self.advanced_analytics_count_left_arm_unknown.setObjectName(u"advanced_analytics_count_left_arm_unknown")
        self.advanced_analytics_count_left_arm_unknown.setGeometry(QRect(1100, 80, 31, 31))
        self.advanced_analytics_count_left_arm_unknown.setFont(font6)
        self.advanced_analytics_count_left_arm_unknown.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.advanced_analytics_count_left_arm_neutral = QLabel(self.page_2)
        self.advanced_analytics_count_left_arm_neutral.setObjectName(u"advanced_analytics_count_left_arm_neutral")
        self.advanced_analytics_count_left_arm_neutral.setGeometry(QRect(1100, 60, 31, 31))
        self.advanced_analytics_count_left_arm_neutral.setFont(font6)
        self.advanced_analytics_count_left_arm_neutral.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.identify_suspicious_check_box_line_graph_advanced_analytics = QCheckBox(self.page_2)
        self.identify_suspicious_check_box_line_graph_advanced_analytics.setObjectName(u"identify_suspicious_check_box_line_graph_advanced_analytics")
        self.identify_suspicious_check_box_line_graph_advanced_analytics.setGeometry(QRect(840, 280, 101, 41))
        self.identify_suspicious_check_box_line_graph_advanced_analytics.setFont(font)
        self.stacked_advanced_analytics.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.time_frame_container_table_event_logs_advanced_analytics = QWidget(self.page_5)
        self.time_frame_container_table_event_logs_advanced_analytics.setObjectName(u"time_frame_container_table_event_logs_advanced_analytics")
        self.time_frame_container_table_event_logs_advanced_analytics.setGeometry(QRect(10, 270, 1131, 61))
        self.time_frame_container_table_event_logs_advanced_analytics.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.play_pause_button_advanced_analytics_table_event_logs = QPushButton(self.page_5)
        self.play_pause_button_advanced_analytics_table_event_logs.setObjectName(u"play_pause_button_advanced_analytics_table_event_logs")
        self.play_pause_button_advanced_analytics_table_event_logs.setGeometry(QRect(950, 230, 191, 41))
        self.play_pause_button_advanced_analytics_table_event_logs.setFont(font9)
        self.play_pause_button_advanced_analytics_table_event_logs.setIcon(icon13)
        self.adv_analytics_preview_event_logs_table_front = QLabel(self.page_5)
        self.adv_analytics_preview_event_logs_table_front.setObjectName(u"adv_analytics_preview_event_logs_table_front")
        self.adv_analytics_preview_event_logs_table_front.setGeometry(QRect(10, 10, 464, 261))
        self.adv_analytics_preview_event_logs_table_front.setFont(font12)
        self.adv_analytics_preview_event_logs_table_front.setFrameShape(QFrame.Shape.WinPanel)
        self.adv_analytics_preview_event_logs_table_front.setFrameShadow(QFrame.Shadow.Raised)
        self.adv_analytics_preview_event_logs_table_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.adv_analytics_preview_event_logs_table_center = QLabel(self.page_5)
        self.adv_analytics_preview_event_logs_table_center.setObjectName(u"adv_analytics_preview_event_logs_table_center")
        self.adv_analytics_preview_event_logs_table_center.setGeometry(QRect(480, 10, 464, 261))
        self.adv_analytics_preview_event_logs_table_center.setFont(font8)
        self.adv_analytics_preview_event_logs_table_center.setFrameShape(QFrame.Shape.WinPanel)
        self.adv_analytics_preview_event_logs_table_center.setFrameShadow(QFrame.Shadow.Raised)
        self.adv_analytics_preview_event_logs_table_center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.advanced_analytics_event_logs_table_1 = QTableWidget(self.page_5)
        if (self.advanced_analytics_event_logs_table_1.columnCount() < 3):
            self.advanced_analytics_event_logs_table_1.setColumnCount(3)
        self.advanced_analytics_event_logs_table_1.setObjectName(u"advanced_analytics_event_logs_table_1")
        self.advanced_analytics_event_logs_table_1.setGeometry(QRect(10, 340, 371, 251))
        self.advanced_analytics_event_logs_table_1.setLineWidth(1)
        self.advanced_analytics_event_logs_table_1.setMidLineWidth(0)
        self.advanced_analytics_event_logs_table_1.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.advanced_analytics_event_logs_table_1.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.advanced_analytics_event_logs_table_1.setGridStyle(Qt.PenStyle.NoPen)
        self.advanced_analytics_event_logs_table_1.setSortingEnabled(True)
        self.advanced_analytics_event_logs_table_1.setColumnCount(3)
        self.advanced_analytics_event_logs_table_1.verticalHeader().setVisible(False)
        self.advanced_analytics_event_logs_table_2 = QTableWidget(self.page_5)
        if (self.advanced_analytics_event_logs_table_2.columnCount() < 3):
            self.advanced_analytics_event_logs_table_2.setColumnCount(3)
        self.advanced_analytics_event_logs_table_2.setObjectName(u"advanced_analytics_event_logs_table_2")
        self.advanced_analytics_event_logs_table_2.setGeometry(QRect(390, 340, 371, 251))
        self.advanced_analytics_event_logs_table_2.setLineWidth(1)
        self.advanced_analytics_event_logs_table_2.setMidLineWidth(0)
        self.advanced_analytics_event_logs_table_2.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.advanced_analytics_event_logs_table_2.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.advanced_analytics_event_logs_table_2.setGridStyle(Qt.PenStyle.NoPen)
        self.advanced_analytics_event_logs_table_2.setSortingEnabled(True)
        self.advanced_analytics_event_logs_table_2.setColumnCount(3)
        self.advanced_analytics_event_logs_table_2.verticalHeader().setVisible(False)
        self.advanced_analytics_event_logs_table_3 = QTableWidget(self.page_5)
        if (self.advanced_analytics_event_logs_table_3.columnCount() < 3):
            self.advanced_analytics_event_logs_table_3.setColumnCount(3)
        self.advanced_analytics_event_logs_table_3.setObjectName(u"advanced_analytics_event_logs_table_3")
        self.advanced_analytics_event_logs_table_3.setGeometry(QRect(770, 340, 371, 251))
        self.advanced_analytics_event_logs_table_3.setLineWidth(1)
        self.advanced_analytics_event_logs_table_3.setMidLineWidth(0)
        self.advanced_analytics_event_logs_table_3.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.advanced_analytics_event_logs_table_3.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.advanced_analytics_event_logs_table_3.setGridStyle(Qt.PenStyle.NoPen)
        self.advanced_analytics_event_logs_table_3.setSortingEnabled(True)
        self.advanced_analytics_event_logs_table_3.setColumnCount(3)
        self.advanced_analytics_event_logs_table_3.verticalHeader().setVisible(False)
        self.front_preview_video_bounding_box_advanced_analytics_event_logs_check_box = QCheckBox(self.page_5)
        self.front_preview_video_bounding_box_advanced_analytics_event_logs_check_box.setObjectName(u"front_preview_video_bounding_box_advanced_analytics_event_logs_check_box")
        self.front_preview_video_bounding_box_advanced_analytics_event_logs_check_box.setGeometry(QRect(310, 12, 121, 20))
        self.label_50 = QLabel(self.page_5)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(480, 10, 161, 21))
        self.label_50.setMaximumSize(QSize(191, 21))
        self.label_50.setFont(font6)
        self.label_50.setAutoFillBackground(False)
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.center_preview_video_bounding_box_advanced_analytics_event_logs_check_box = QCheckBox(self.page_5)
        self.center_preview_video_bounding_box_advanced_analytics_event_logs_check_box.setObjectName(u"center_preview_video_bounding_box_advanced_analytics_event_logs_check_box")
        self.center_preview_video_bounding_box_advanced_analytics_event_logs_check_box.setGeometry(QRect(780, 12, 121, 20))
        self.label_51 = QLabel(self.page_5)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(10, 10, 161, 21))
        self.label_51.setMaximumSize(QSize(191, 21))
        self.label_51.setFont(font6)
        self.label_51.setAutoFillBackground(False)
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.center_preview_video_keypoints_advanced_analytics_event_logs_check_box = QCheckBox(self.page_5)
        self.center_preview_video_keypoints_advanced_analytics_event_logs_check_box.setObjectName(u"center_preview_video_keypoints_advanced_analytics_event_logs_check_box")
        self.center_preview_video_keypoints_advanced_analytics_event_logs_check_box.setGeometry(QRect(670, 12, 81, 20))
        self.front_preview_video_keypoints_advanced_analytics_event_logs_check_box = QCheckBox(self.page_5)
        self.front_preview_video_keypoints_advanced_analytics_event_logs_check_box.setObjectName(u"front_preview_video_keypoints_advanced_analytics_event_logs_check_box")
        self.front_preview_video_keypoints_advanced_analytics_event_logs_check_box.setGeometry(QRect(200, 12, 81, 20))
        self.stacked_advanced_analytics.addWidget(self.page_5)
        self.time_frame_container_table_event_logs_advanced_analytics.raise_()
        self.play_pause_button_advanced_analytics_table_event_logs.raise_()
        self.adv_analytics_preview_event_logs_table_front.raise_()
        self.adv_analytics_preview_event_logs_table_center.raise_()
        self.advanced_analytics_event_logs_table_1.raise_()
        self.advanced_analytics_event_logs_table_2.raise_()
        self.advanced_analytics_event_logs_table_3.raise_()
        self.front_preview_video_bounding_box_advanced_analytics_event_logs_check_box.raise_()
        self.label_50.raise_()
        self.label_51.raise_()
        self.center_preview_video_keypoints_advanced_analytics_event_logs_check_box.raise_()
        self.front_preview_video_keypoints_advanced_analytics_event_logs_check_box.raise_()
        self.center_preview_video_bounding_box_advanced_analytics_event_logs_check_box.raise_()
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_77 = QLabel(self.page_7)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setGeometry(QRect(940, 140, 181, 41))
        self.label_77.setFont(font6)
        self.label_78 = QLabel(self.page_7)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setGeometry(QRect(940, 40, 131, 31))
        self.label_78.setFont(font6)
        self.label_79 = QLabel(self.page_7)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setGeometry(QRect(940, 10, 201, 31))
        self.label_79.setFont(font16)
        self.label_79.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_80 = QLabel(self.page_7)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setGeometry(QRect(940, 90, 131, 31))
        self.label_80.setFont(font6)
        self.interval_time_label_advanced_analytics = QLabel(self.page_7)
        self.interval_time_label_advanced_analytics.setObjectName(u"interval_time_label_advanced_analytics")
        self.interval_time_label_advanced_analytics.setGeometry(QRect(940, 170, 201, 31))
        self.interval_time_label_advanced_analytics.setFont(font)
        self.interval_time_label_advanced_analytics.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.front_preview_video_bounding_box_advanced_analytics_event_summary_check_box = QCheckBox(self.page_7)
        self.front_preview_video_bounding_box_advanced_analytics_event_summary_check_box.setObjectName(u"front_preview_video_bounding_box_advanced_analytics_event_summary_check_box")
        self.front_preview_video_bounding_box_advanced_analytics_event_summary_check_box.setGeometry(QRect(300, 12, 221, 20))
        self.front_preview_video_bounding_box_advanced_analytics_event_summary_check_box.setAutoFillBackground(False)
        self.advanced_analytics_chunk_summary_preview_front = QLabel(self.page_7)
        self.advanced_analytics_chunk_summary_preview_front.setObjectName(u"advanced_analytics_chunk_summary_preview_front")
        self.advanced_analytics_chunk_summary_preview_front.setGeometry(QRect(10, 10, 461, 260))
        self.advanced_analytics_chunk_summary_preview_front.setFont(font12)
        self.advanced_analytics_chunk_summary_preview_front.setStyleSheet(u"")
        self.advanced_analytics_chunk_summary_preview_front.setFrameShape(QFrame.Shape.WinPanel)
        self.advanced_analytics_chunk_summary_preview_front.setFrameShadow(QFrame.Shadow.Raised)
        self.advanced_analytics_chunk_summary_preview_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_81 = QLabel(self.page_7)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setGeometry(QRect(10, 10, 161, 21))
        self.label_81.setMaximumSize(QSize(191, 21))
        self.label_81.setFont(font6)
        self.label_81.setAutoFillBackground(False)
        self.label_81.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.advanced_analytics_interval_slider_seconds = QSlider(self.page_7)
        self.advanced_analytics_interval_slider_seconds.setObjectName(u"advanced_analytics_interval_slider_seconds")
        self.advanced_analytics_interval_slider_seconds.setGeometry(QRect(940, 110, 201, 31))
        self.advanced_analytics_interval_slider_seconds.setMaximum(60)
        self.advanced_analytics_interval_slider_seconds.setValue(2)
        self.advanced_analytics_interval_slider_seconds.setOrientation(Qt.Orientation.Horizontal)
        self.label_82 = QLabel(self.page_7)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setGeometry(QRect(470, 10, 161, 21))
        self.label_82.setMaximumSize(QSize(191, 21))
        self.label_82.setFont(font6)
        self.label_82.setAutoFillBackground(False)
        self.label_82.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.advanced_analytics_event_summary_table = QTableWidget(self.page_7)
        if (self.advanced_analytics_event_summary_table.columnCount() < 2):
            self.advanced_analytics_event_summary_table.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font14);
        self.advanced_analytics_event_summary_table.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font15);
        self.advanced_analytics_event_summary_table.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.advanced_analytics_event_summary_table.setObjectName(u"advanced_analytics_event_summary_table")
        self.advanced_analytics_event_summary_table.setGeometry(QRect(10, 320, 1131, 271))
        self.advanced_analytics_event_summary_table.setFont(font6)
        self.advanced_analytics_event_summary_table.setLineWidth(1)
        self.advanced_analytics_event_summary_table.setMidLineWidth(0)
        self.advanced_analytics_event_summary_table.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.advanced_analytics_event_summary_table.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.advanced_analytics_event_summary_table.setGridStyle(Qt.PenStyle.NoPen)
        self.advanced_analytics_event_summary_table.setSortingEnabled(True)
        self.advanced_analytics_event_summary_table.setRowCount(0)
        self.advanced_analytics_event_summary_table.setColumnCount(2)
        self.advanced_analytics_event_summary_table.verticalHeader().setVisible(False)
        self.advanced_analytics_event_summary_play_pause_button = QPushButton(self.page_7)
        self.advanced_analytics_event_summary_play_pause_button.setObjectName(u"advanced_analytics_event_summary_play_pause_button")
        self.advanced_analytics_event_summary_play_pause_button.setGeometry(QRect(940, 225, 201, 41))
        self.advanced_analytics_event_summary_play_pause_button.setFont(font9)
        self.advanced_analytics_event_summary_play_pause_button.setIcon(icon13)
        self.center_preview_video_bounding_box_advanced_analytics_event_summary_check_box = QCheckBox(self.page_7)
        self.center_preview_video_bounding_box_advanced_analytics_event_summary_check_box.setObjectName(u"center_preview_video_bounding_box_advanced_analytics_event_summary_check_box")
        self.center_preview_video_bounding_box_advanced_analytics_event_summary_check_box.setGeometry(QRect(780, 12, 201, 20))
        self.center_preview_video_bounding_box_advanced_analytics_event_summary_check_box.setAutoFillBackground(False)
        self.advanced_analytics_chunk_summary_preview_center = QLabel(self.page_7)
        self.advanced_analytics_chunk_summary_preview_center.setObjectName(u"advanced_analytics_chunk_summary_preview_center")
        self.advanced_analytics_chunk_summary_preview_center.setGeometry(QRect(470, 10, 461, 260))
        self.advanced_analytics_chunk_summary_preview_center.setFont(font8)
        self.advanced_analytics_chunk_summary_preview_center.setFrameShape(QFrame.Shape.WinPanel)
        self.advanced_analytics_chunk_summary_preview_center.setFrameShadow(QFrame.Shadow.Raised)
        self.advanced_analytics_chunk_summary_preview_center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.center_preview_video_keypoints_advanced_analytics_event_summary_check_box = QCheckBox(self.page_7)
        self.center_preview_video_keypoints_advanced_analytics_event_summary_check_box.setObjectName(u"center_preview_video_keypoints_advanced_analytics_event_summary_check_box")
        self.center_preview_video_keypoints_advanced_analytics_event_summary_check_box.setGeometry(QRect(670, 12, 91, 20))
        self.center_preview_video_keypoints_advanced_analytics_event_summary_check_box.setAutoFillBackground(False)
        self.time_frame_container_table_event_summary_advanced_analytics = QWidget(self.page_7)
        self.time_frame_container_table_event_summary_advanced_analytics.setObjectName(u"time_frame_container_table_event_summary_advanced_analytics")
        self.time_frame_container_table_event_summary_advanced_analytics.setGeometry(QRect(0, 270, 1151, 51))
        self.time_frame_container_table_event_summary_advanced_analytics.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.advanced_analytics_interval_slider_minutes = QSlider(self.page_7)
        self.advanced_analytics_interval_slider_minutes.setObjectName(u"advanced_analytics_interval_slider_minutes")
        self.advanced_analytics_interval_slider_minutes.setGeometry(QRect(940, 60, 201, 31))
        self.advanced_analytics_interval_slider_minutes.setMaximum(5)
        self.advanced_analytics_interval_slider_minutes.setOrientation(Qt.Orientation.Horizontal)
        self.front_preview_video_keypoints_advanced_analytics_event_summary_check_box = QCheckBox(self.page_7)
        self.front_preview_video_keypoints_advanced_analytics_event_summary_check_box.setObjectName(u"front_preview_video_keypoints_advanced_analytics_event_summary_check_box")
        self.front_preview_video_keypoints_advanced_analytics_event_summary_check_box.setGeometry(QRect(200, 12, 81, 20))
        self.front_preview_video_keypoints_advanced_analytics_event_summary_check_box.setAutoFillBackground(False)
        self.stacked_advanced_analytics.addWidget(self.page_7)
        self.advanced_analytics_chunk_summary_preview_center.raise_()
        self.label_77.raise_()
        self.label_78.raise_()
        self.label_79.raise_()
        self.label_80.raise_()
        self.interval_time_label_advanced_analytics.raise_()
        self.advanced_analytics_chunk_summary_preview_front.raise_()
        self.advanced_analytics_interval_slider_seconds.raise_()
        self.label_82.raise_()
        self.advanced_analytics_event_summary_table.raise_()
        self.advanced_analytics_event_summary_play_pause_button.raise_()
        self.time_frame_container_table_event_summary_advanced_analytics.raise_()
        self.advanced_analytics_interval_slider_minutes.raise_()
        self.front_preview_video_bounding_box_advanced_analytics_event_summary_check_box.raise_()
        self.front_preview_video_keypoints_advanced_analytics_event_summary_check_box.raise_()
        self.label_81.raise_()
        self.center_preview_video_bounding_box_advanced_analytics_event_summary_check_box.raise_()
        self.center_preview_video_keypoints_advanced_analytics_event_summary_check_box.raise_()
        self.advanced_analytics_visualization_combo_box = QComboBox(self.page)
        self.advanced_analytics_visualization_combo_box.addItem("")
        self.advanced_analytics_visualization_combo_box.addItem("")
        self.advanced_analytics_visualization_combo_box.addItem("")
        self.advanced_analytics_visualization_combo_box.addItem("")
        self.advanced_analytics_visualization_combo_box.setObjectName(u"advanced_analytics_visualization_combo_box")
        self.advanced_analytics_visualization_combo_box.setGeometry(QRect(920, 10, 221, 51))
        self.advanced_analytics_visualization_combo_box.setFont(font3)
        self.label_25 = QLabel(self.page)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(10, 0, 721, 61))
        self.label_25.setFont(font4)
        self.label_38 = QLabel(self.page)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(800, 10, 121, 51))
        self.label_38.setFont(font6)
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.stackedPanels.addWidget(self.page)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_34 = QLabel(self.page_6)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 0, 631, 61))
        self.label_34.setFont(font4)
        self.frame_6 = QFrame(self.page_6)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 70, 1131, 581))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.generate_document_report = QPushButton(self.frame_6)
        self.generate_document_report.setObjectName(u"generate_document_report")
        self.generate_document_report.setGeometry(QRect(560, 50, 131, 41))
        self.generate_document_report.setFont(font3)
        icon15 = QIcon()
        icon15.addFile(u":/icons/document-2-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.generate_document_report.setIcon(icon15)
        self.generate_document_report.setIconSize(QSize(20, 20))
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 50, 301, 41))
        self.label_16.setFont(font3)
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.media_settings_frame = QFrame(self.frame_6)
        self.media_settings_frame.setObjectName(u"media_settings_frame")
        self.media_settings_frame.setGeometry(QRect(10, 110, 1111, 271))
        self.media_settings_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.media_settings_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_7 = QFrame(self.media_settings_frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(140, 60, 311, 51))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.ai_analytics_export_radio_button = QRadioButton(self.frame_7)
        self.ai_analytics_export_radio_button.setObjectName(u"ai_analytics_export_radio_button")
        self.ai_analytics_export_radio_button.setEnabled(True)
        self.ai_analytics_export_radio_button.setGeometry(QRect(10, 10, 131, 31))
        self.ai_analytics_export_radio_button.setFont(font6)
        self.ai_analytics_export_radio_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ai_analytics_export_radio_button.setChecked(True)
        self.advanced_analytics_export_radio_button = QRadioButton(self.frame_7)
        self.advanced_analytics_export_radio_button.setObjectName(u"advanced_analytics_export_radio_button")
        self.advanced_analytics_export_radio_button.setGeometry(QRect(130, 10, 201, 31))
        self.advanced_analytics_export_radio_button.setFont(font6)
        self.advanced_analytics_export_radio_button.setChecked(False)
        self.camera_angles_group_frame = QFrame(self.media_settings_frame)
        self.camera_angles_group_frame.setObjectName(u"camera_angles_group_frame")
        self.camera_angles_group_frame.setEnabled(False)
        self.camera_angles_group_frame.setGeometry(QRect(250, 160, 621, 51))
        self.camera_angles_group_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.camera_angles_group_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.front_video_only_radio_button = QRadioButton(self.camera_angles_group_frame)
        self.front_video_only_radio_button.setObjectName(u"front_video_only_radio_button")
        self.front_video_only_radio_button.setGeometry(QRect(20, 0, 151, 51))
        self.front_video_only_radio_button.setFont(font6)
        self.front_video_only_radio_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.front_video_only_radio_button.setChecked(False)
        self.center_video_only_radio_button = QRadioButton(self.camera_angles_group_frame)
        self.center_video_only_radio_button.setObjectName(u"center_video_only_radio_button")
        self.center_video_only_radio_button.setGeometry(QRect(200, 0, 181, 51))
        self.center_video_only_radio_button.setFont(font6)
        self.center_video_only_radio_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.both_front_and_center_video_button = QRadioButton(self.camera_angles_group_frame)
        self.both_front_and_center_video_button.setObjectName(u"both_front_and_center_video_button")
        self.both_front_and_center_video_button.setGeometry(QRect(360, 0, 261, 51))
        self.both_front_and_center_video_button.setFont(font6)
        self.both_front_and_center_video_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.both_front_and_center_video_button.setChecked(True)
        self.label_20 = QLabel(self.media_settings_frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 0, 1111, 71))
        self.label_20.setFont(font5)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_21 = QLabel(self.media_settings_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(0, 130, 1111, 31))
        self.label_21.setFont(font5)
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.drawing_options_group_frame = QFrame(self.media_settings_frame)
        self.drawing_options_group_frame.setObjectName(u"drawing_options_group_frame")
        self.drawing_options_group_frame.setEnabled(True)
        self.drawing_options_group_frame.setGeometry(QRect(470, 60, 491, 51))
        self.drawing_options_group_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.drawing_options_group_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.add_keypoints_check_box = QCheckBox(self.drawing_options_group_frame)
        self.add_keypoints_check_box.setObjectName(u"add_keypoints_check_box")
        self.add_keypoints_check_box.setEnabled(True)
        self.add_keypoints_check_box.setGeometry(QRect(10, 0, 141, 51))
        self.add_keypoints_check_box.setFont(font6)
        self.add_bounding_box_check_box = QCheckBox(self.drawing_options_group_frame)
        self.add_bounding_box_check_box.setObjectName(u"add_bounding_box_check_box")
        self.add_bounding_box_check_box.setEnabled(True)
        self.add_bounding_box_check_box.setGeometry(QRect(150, 0, 171, 51))
        self.add_bounding_box_check_box.setFont(font6)
        self.suspicious_movements_option_export = QCheckBox(self.drawing_options_group_frame)
        self.suspicious_movements_option_export.setObjectName(u"suspicious_movements_option_export")
        self.suspicious_movements_option_export.setEnabled(True)
        self.suspicious_movements_option_export.setGeometry(QRect(310, 0, 171, 51))
        self.suspicious_movements_option_export.setFont(font6)
        self.export_progress_bar = QProgressBar(self.media_settings_frame)
        self.export_progress_bar.setObjectName(u"export_progress_bar")
        self.export_progress_bar.setGeometry(QRect(10, 220, 1091, 31))
        self.export_progress_bar.setAutoFillBackground(False)
        self.export_progress_bar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #880000;\n"
"    border-radius: 6px;\n"
"    background-color: #f0f0f0;\n"
"    text-align: center;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 1, y2: 0,\n"
"        stop: 0 #cc0000, \n"
"        stop: 1 #990000\n"
"    );\n"
"    border-radius: 6px;\n"
"    margin: 1px;\n"
"}\n"
"")
        self.export_progress_bar.setValue(0)
        self.export_progress_bar.setTextVisible(False)
        self.document_export_combo_box = QComboBox(self.frame_6)
        self.document_export_combo_box.addItem("")
        self.document_export_combo_box.addItem("")
        self.document_export_combo_box.addItem("")
        self.document_export_combo_box.setObjectName(u"document_export_combo_box")
        self.document_export_combo_box.setGeometry(QRect(190, 50, 351, 41))
        self.document_export_combo_box.setFont(font6)
        self.send_to_email_button = QPushButton(self.frame_6)
        self.send_to_email_button.setObjectName(u"send_to_email_button")
        self.send_to_email_button.setEnabled(False)
        self.send_to_email_button.setGeometry(QRect(710, 50, 231, 41))
        self.send_to_email_button.setFont(font3)
        icon16 = QIcon()
        icon16.addFile(u":/icons/email-12-256.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.send_to_email_button.setIcon(icon16)
        self.send_to_email_button.setIconSize(QSize(20, 20))
        self.stackedPanels.addWidget(self.page_6)
        self.TutorialPage = QWidget()
        self.TutorialPage.setObjectName(u"TutorialPage")
        self.frame_11 = QFrame(self.TutorialPage)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 70, 591, 571))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 281, 41))
        self.label_2.setFont(font)
        self.stepbystepTutorial_text = QTextEdit(self.frame_11)
        self.stepbystepTutorial_text.setObjectName(u"stepbystepTutorial_text")
        self.stepbystepTutorial_text.setGeometry(QRect(10, 50, 571, 431))
        self.frame_12 = QFrame(self.TutorialPage)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(603, 70, 541, 571))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 221, 41))
        self.label_3.setFont(font)
        self.Back_to_Home_button = QPushButton(self.frame_12)
        self.Back_to_Home_button.setObjectName(u"Back_to_Home_button")
        self.Back_to_Home_button.setGeometry(QRect(350, 500, 181, 51))
        self.Back_to_Home_button.setFont(font6)
        self.Back_to_Home_button.setIcon(icon9)
        self.Back_to_Home_button.setIconSize(QSize(20, 20))
        self.stepbystepTutorial_text_2 = QTextEdit(self.frame_12)
        self.stepbystepTutorial_text_2.setObjectName(u"stepbystepTutorial_text_2")
        self.stepbystepTutorial_text_2.setGeometry(QRect(10, 50, 521, 431))
        self.label_66 = QLabel(self.TutorialPage)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(10, 0, 271, 71))
        self.label_66.setFont(font4)
        self.stackedPanels.addWidget(self.TutorialPage)
        self.DatasetPage = QWidget()
        self.DatasetPage.setObjectName(u"DatasetPage")
        self.frame_2 = QFrame(self.DatasetPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 120, 901, 381))
        self.frame_2.setFrameShape(QFrame.Shape.Box)
        self.frame_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_2.setLineWidth(2)
        self.status_label = QLabel(self.frame_2)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(70, 20, 131, 21))
        palette = QPalette()
        brush = QBrush(QColor(0, 255, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(245, 245, 245, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush2 = QBrush(QColor(0, 255, 0, 128))
        brush2.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        brush3 = QBrush(QColor(0, 255, 0, 128))
        brush3.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        brush4 = QBrush(QColor(0, 255, 0, 128))
        brush4.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush4)
#endif
        self.status_label.setPalette(palette)
        self.status_label.setFont(font)
        self.status_label.setStyleSheet(u"color: rgb(0, 255, 0);")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 20, 51, 21))
        self.label_12.setFont(font6)
        self.label_12.setAutoFillBackground(False)
        self.camera_feed = QLabel(self.frame_2)
        self.camera_feed.setObjectName(u"camera_feed")
        self.camera_feed.setGeometry(QRect(10, 10, 443, 300))
        self.camera_feed.setMaximumSize(QSize(450, 300))
        self.camera_feed.setFont(font12)
        self.camera_feed.setFrameShape(QFrame.Shape.WinPanel)
        self.camera_feed.setFrameShadow(QFrame.Shadow.Raised)
        self.camera_feed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.white_frame_feed = QLabel(self.frame_2)
        self.white_frame_feed.setObjectName(u"white_frame_feed")
        self.white_frame_feed.setGeometry(QRect(450, 10, 443, 300))
        self.white_frame_feed.setMaximumSize(QSize(450, 300))
        self.white_frame_feed.setFont(font12)
        self.white_frame_feed.setFrameShape(QFrame.Shape.WinPanel)
        self.white_frame_feed.setFrameShadow(QFrame.Shadow.Raised)
        self.white_frame_feed.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 310, 441, 28))
        self.label.setMaximumSize(QSize(451, 31))
        self.label.setFont(font8)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(450, 310, 441, 28))
        self.label_4.setMaximumSize(QSize(451, 31))
        self.label_4.setFont(font8)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.showCameraLandmarksChkBox = QCheckBox(self.frame_2)
        self.showCameraLandmarksChkBox.setObjectName(u"showCameraLandmarksChkBox")
        self.showCameraLandmarksChkBox.setGeometry(QRect(10, 340, 212, 26))
        self.showCameraLandmarksChkBox.setMaximumSize(QSize(221, 31))
        self.showCameraLandmarksChkBox.setFont(font6)
        self.showCameraLandmarksChkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_whiteframe_boundingbox = QCheckBox(self.frame_2)
        self.show_whiteframe_boundingbox.setObjectName(u"show_whiteframe_boundingbox")
        self.show_whiteframe_boundingbox.setGeometry(QRect(460, 340, 209, 26))
        self.show_whiteframe_boundingbox.setMaximumSize(QSize(221, 31))
        self.show_whiteframe_boundingbox.setFont(font6)
        self.show_whiteframe_boundingbox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.showCameraBoundingBoxChkBox = QCheckBox(self.frame_2)
        self.showCameraBoundingBoxChkBox.setObjectName(u"showCameraBoundingBoxChkBox")
        self.showCameraBoundingBoxChkBox.setGeometry(QRect(170, 340, 141, 26))
        self.showCameraBoundingBoxChkBox.setMaximumSize(QSize(221, 31))
        self.showCameraBoundingBoxChkBox.setFont(font6)
        self.showCameraBoundingBoxChkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_skeleton_camera = QCheckBox(self.frame_2)
        self.show_skeleton_camera.setObjectName(u"show_skeleton_camera")
        self.show_skeleton_camera.setGeometry(QRect(320, 340, 131, 26))
        self.show_skeleton_camera.setMaximumSize(QSize(221, 31))
        self.show_skeleton_camera.setFont(font6)
        self.show_skeleton_camera.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.darkMode_whiteframe = QCheckBox(self.frame_2)
        self.darkMode_whiteframe.setObjectName(u"darkMode_whiteframe")
        self.darkMode_whiteframe.setGeometry(QRect(620, 340, 116, 26))
        self.darkMode_whiteframe.setMaximumSize(QSize(221, 31))
        self.darkMode_whiteframe.setFont(font6)
        self.darkMode_whiteframe.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.show_skeleton_white_frame = QCheckBox(self.frame_2)
        self.show_skeleton_white_frame.setObjectName(u"show_skeleton_white_frame")
        self.show_skeleton_white_frame.setGeometry(QRect(720, 340, 166, 26))
        self.show_skeleton_white_frame.setMaximumSize(QSize(221, 31))
        self.show_skeleton_white_frame.setFont(font6)
        self.show_skeleton_white_frame.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_feed.raise_()
        self.white_frame_feed.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_12.raise_()
        self.show_whiteframe_boundingbox.raise_()
        self.darkMode_whiteframe.raise_()
        self.show_skeleton_white_frame.raise_()
        self.status_label.raise_()
        self.showCameraLandmarksChkBox.raise_()
        self.showCameraBoundingBoxChkBox.raise_()
        self.show_skeleton_camera.raise_()
        self.frame_4 = QFrame(self.DatasetPage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 510, 901, 141))
        self.frame_4.setFrameShape(QFrame.Shape.Box)
        self.frame_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_4.setLineWidth(2)
        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(13, 29, 79, 28))
        self.label_7.setMaximumSize(QSize(81, 28))
        self.label_7.setFont(font6)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.action_comboBox = QComboBox(self.frame_4)
        self.action_comboBox.setObjectName(u"action_comboBox")
        self.action_comboBox.setGeometry(QRect(100, 26, 371, 41))
        self.action_comboBox.setFont(font6)
        self.action_comboBox.setEditable(True)
        self.refresh_button = QPushButton(self.frame_4)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setGeometry(QRect(481, 30, 101, 31))
        self.refresh_button.setFont(font6)
        self.recording_button = QPushButton(self.frame_4)
        self.recording_button.setObjectName(u"recording_button")
        self.recording_button.setGeometry(QRect(640, 20, 241, 101))
        palette1 = QPalette()
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush5)
        gradient = QLinearGradient(0, 0, 0, 1)
        gradient.setSpread(QGradient.Spread.PadSpread)
        gradient.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(67, 215, 122, 255))
        gradient.setColorAt(1, QColor(52, 192, 101, 255))
        brush6 = QBrush(gradient)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush6)
        brush7 = QBrush(QColor(170, 255, 255, 255))
        brush7.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Light, brush7)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush5)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush5)
        gradient1 = QLinearGradient(0, 0, 0, 1)
        gradient1.setSpread(QGradient.Spread.PadSpread)
        gradient1.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(67, 215, 122, 255))
        gradient1.setColorAt(1, QColor(52, 192, 101, 255))
        brush8 = QBrush(gradient1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush8)
        gradient2 = QLinearGradient(0, 0, 0, 1)
        gradient2.setSpread(QGradient.Spread.PadSpread)
        gradient2.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(67, 215, 122, 255))
        gradient2.setColorAt(1, QColor(52, 192, 101, 255))
        brush9 = QBrush(gradient2)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush9)
        brush10 = QBrush(QColor(0, 0, 0, 128))
        brush10.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush10)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush5)
        gradient3 = QLinearGradient(0, 0, 0, 1)
        gradient3.setSpread(QGradient.Spread.PadSpread)
        gradient3.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(67, 215, 122, 255))
        gradient3.setColorAt(1, QColor(52, 192, 101, 255))
        brush11 = QBrush(gradient3)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush11)
        brush12 = QBrush(QColor(255, 255, 255, 255))
        brush12.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Light, brush12)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush5)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush5)
        gradient4 = QLinearGradient(0, 0, 0, 1)
        gradient4.setSpread(QGradient.Spread.PadSpread)
        gradient4.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(67, 215, 122, 255))
        gradient4.setColorAt(1, QColor(52, 192, 101, 255))
        brush13 = QBrush(gradient4)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush13)
        gradient5 = QLinearGradient(0, 0, 0, 1)
        gradient5.setSpread(QGradient.Spread.PadSpread)
        gradient5.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(67, 215, 122, 255))
        gradient5.setColorAt(1, QColor(52, 192, 101, 255))
        brush14 = QBrush(gradient5)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush14)
        brush15 = QBrush(QColor(0, 0, 0, 128))
        brush15.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush15)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush5)
        gradient6 = QLinearGradient(0, 0, 0, 1)
        gradient6.setSpread(QGradient.Spread.PadSpread)
        gradient6.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(67, 215, 122, 255))
        gradient6.setColorAt(1, QColor(52, 192, 101, 255))
        brush16 = QBrush(gradient6)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush16)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Light, brush12)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush5)
        brush17 = QBrush(QColor(0, 0, 0, 92))
        brush17.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush17)
        gradient7 = QLinearGradient(0, 0, 0, 1)
        gradient7.setSpread(QGradient.Spread.PadSpread)
        gradient7.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(67, 215, 122, 255))
        gradient7.setColorAt(1, QColor(52, 192, 101, 255))
        brush18 = QBrush(gradient7)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush18)
        gradient8 = QLinearGradient(0, 0, 0, 1)
        gradient8.setSpread(QGradient.Spread.PadSpread)
        gradient8.setCoordinateMode(QGradient.CoordinateMode.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(67, 215, 122, 255))
        gradient8.setColorAt(1, QColor(52, 192, 101, 255))
        brush19 = QBrush(gradient8)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush19)
        brush20 = QBrush(QColor(0, 0, 0, 128))
        brush20.setStyle(Qt.BrushStyle.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush20)
#endif
        self.recording_button.setPalette(palette1)
        self.recording_button.setFont(font9)
        self.recording_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.recording_button.setStyleSheet(u"")
        self.add_action_button = QPushButton(self.frame_4)
        self.add_action_button.setObjectName(u"add_action_button")
        self.add_action_button.setGeometry(QRect(146, 80, 101, 31))
        self.add_action_button.setFont(font6)
        self.delete_action_button = QPushButton(self.frame_4)
        self.delete_action_button.setObjectName(u"delete_action_button")
        self.delete_action_button.setGeometry(QRect(316, 80, 101, 31))
        self.delete_action_button.setFont(font6)
        self.groupBox = QGroupBox(self.DatasetPage)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(920, 110, 221, 541))
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:2 rgba(255, 255, 255, 255));")
        self.groupBox.setFlat(False)
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.interval_label = QLabel(self.groupBox)
        self.interval_label.setObjectName(u"interval_label")
        self.interval_label.setMaximumSize(QSize(41, 41))
        self.interval_label.setFont(font)
        self.interval_label.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.interval_label.setFrameShape(QFrame.Shape.Box)
        self.interval_label.setFrameShadow(QFrame.Shadow.Sunken)
        self.interval_label.setLineWidth(1)
        self.interval_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.interval_label.setMargin(0)

        self.gridLayout_5.addWidget(self.interval_label, 7, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(121, 21))
        self.label_8.setFont(font6)

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)

        self.refresh_action_list = QPushButton(self.groupBox)
        self.refresh_action_list.setObjectName(u"refresh_action_list")
        self.refresh_action_list.setMaximumSize(QSize(91, 31))
        self.refresh_action_list.setFont(font6)
        self.refresh_action_list.setAutoExclusive(True)

        self.gridLayout_5.addWidget(self.refresh_action_list, 4, 0, 1, 1)

        self.action_table = QTableWidget(self.groupBox)
        if (self.action_table.columnCount() < 2):
            self.action_table.setColumnCount(2)
        if (self.action_table.rowCount() < 7):
            self.action_table.setRowCount(7)
        self.action_table.setObjectName(u"action_table")
        self.action_table.setMaximumSize(QSize(261, 181))
        self.action_table.setFrameShape(QFrame.Shape.WinPanel)
        self.action_table.setFrameShadow(QFrame.Shadow.Raised)
        self.action_table.setLineWidth(2)
        self.action_table.setAutoScrollMargin(9)
        self.action_table.setProperty(u"showDropIndicator", False)
        self.action_table.setDragEnabled(False)
        self.action_table.setDragDropOverwriteMode(False)
        self.action_table.setShowGrid(True)
        self.action_table.setGridStyle(Qt.PenStyle.SolidLine)
        self.action_table.setSortingEnabled(False)
        self.action_table.setWordWrap(True)
        self.action_table.setCornerButtonEnabled(False)
        self.action_table.setRowCount(7)
        self.action_table.setColumnCount(2)
        self.action_table.horizontalHeader().setCascadingSectionResizes(False)
        self.action_table.horizontalHeader().setMinimumSectionSize(37)
        self.action_table.horizontalHeader().setDefaultSectionSize(111)
        self.action_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.action_table.verticalHeader().setVisible(False)
        self.action_table.verticalHeader().setDefaultSectionSize(27)

        self.gridLayout_5.addWidget(self.action_table, 3, 0, 1, 2)

        self.sequence_label = QLabel(self.groupBox)
        self.sequence_label.setObjectName(u"sequence_label")
        self.sequence_label.setMaximumSize(QSize(41, 41))
        self.sequence_label.setFont(font)
        self.sequence_label.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.sequence_label.setFrameShape(QFrame.Shape.Box)
        self.sequence_label.setFrameShadow(QFrame.Shadow.Sunken)
        self.sequence_label.setLineWidth(1)
        self.sequence_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sequence_label.setMargin(0)

        self.gridLayout_5.addWidget(self.sequence_label, 9, 1, 1, 1)

        self.interval_slider = QSlider(self.groupBox)
        self.interval_slider.setObjectName(u"interval_slider")
        self.interval_slider.setMaximumSize(QSize(211, 21))
        self.interval_slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.interval_slider.setMinimum(1)
        self.interval_slider.setMaximum(10)
        self.interval_slider.setSliderPosition(3)
        self.interval_slider.setOrientation(Qt.Orientation.Horizontal)
        self.interval_slider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout_5.addWidget(self.interval_slider, 7, 0, 1, 1)

        self.directoryLineEdit = QLineEdit(self.groupBox)
        self.directoryLineEdit.setObjectName(u"directoryLineEdit")
        self.directoryLineEdit.setMaximumSize(QSize(261, 31))
        self.directoryLineEdit.setFont(font8)

        self.gridLayout_5.addWidget(self.directoryLineEdit, 1, 0, 1, 2)

        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(171, 21))
        self.label_13.setFont(font6)
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_13, 8, 0, 1, 1)

        self.browseButton = QPushButton(self.groupBox)
        self.browseButton.setObjectName(u"browseButton")
        self.browseButton.setMaximumSize(QSize(91, 31))
        self.browseButton.setFont(font6)

        self.gridLayout_5.addWidget(self.browseButton, 2, 0, 1, 1)

        self.sequence_slider = QSlider(self.groupBox)
        self.sequence_slider.setObjectName(u"sequence_slider")
        self.sequence_slider.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.sequence_slider.setMinimum(1)
        self.sequence_slider.setMaximum(60)
        self.sequence_slider.setValue(30)
        self.sequence_slider.setSliderPosition(30)
        self.sequence_slider.setOrientation(Qt.Orientation.Horizontal)
        self.sequence_slider.setTickPosition(QSlider.TickPosition.TicksAbove)

        self.gridLayout_5.addWidget(self.sequence_slider, 9, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(151, 21))
        self.label_11.setFont(font3)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_11, 6, 0, 1, 1)

        self.frame_3 = QFrame(self.DatasetPage)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 60, 1131, 51))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label_Camera = QLabel(self.frame_3)
        self.label_Camera.setObjectName(u"label_Camera")
        self.label_Camera.setGeometry(QRect(10, 0, 61, 51))
        self.label_Camera.setFont(font6)
        self.cameraComboBox = QComboBox(self.frame_3)
        self.cameraComboBox.setObjectName(u"cameraComboBox")
        self.cameraComboBox.setGeometry(QRect(60, 10, 211, 31))
        self.cameraComboBox.setFont(font6)
        self.cameraComboBox.setEditable(True)
        self.openCamera = QPushButton(self.frame_3)
        self.openCamera.setObjectName(u"openCamera")
        self.openCamera.setGeometry(QRect(280, 10, 121, 31))
        self.openCamera.setFont(font6)
        self.closeCamera = QPushButton(self.frame_3)
        self.closeCamera.setObjectName(u"closeCamera")
        self.closeCamera.setGeometry(QRect(410, 10, 121, 31))
        self.closeCamera.setFont(font6)
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(550, 0, 24, 18))
        self.label_10.setFont(font6)
        self.fps_label = QLabel(self.frame_3)
        self.fps_label.setObjectName(u"fps_label")
        self.fps_label.setGeometry(QRect(570, 0, 81, 51))
        palette2 = QPalette()
        brush21 = QBrush(QColor(170, 85, 255, 255))
        brush21.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush21)
        brush22 = QBrush(QColor(0, 0, 0, 0))
        brush22.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush22)
        brush23 = QBrush(QColor(226, 112, 255, 255))
        brush23.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush23)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush23)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush22)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush22)
        brush24 = QBrush(QColor(226, 112, 255, 128))
        brush24.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush24)
#endif
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush21)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush22)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush23)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush23)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush22)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush24)
#endif
        brush25 = QBrush(QColor(120, 120, 120, 255))
        brush25.setStyle(Qt.BrushStyle.SolidPattern)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush25)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush22)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush23)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush23)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush22)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush24)
#endif
        self.fps_label.setPalette(palette2)
        self.fps_label.setFont(font)
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(660, 0, 64, 20))
        self.label_5.setFont(font6)
        self.cpu_label = QLabel(self.frame_3)
        self.cpu_label.setObjectName(u"cpu_label")
        self.cpu_label.setGeometry(QRect(730, 0, 81, 51))
        palette3 = QPalette()
        brush26 = QBrush(QColor(0, 85, 255, 255))
        brush26.setStyle(Qt.BrushStyle.SolidPattern)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush26)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush22)
        brush27 = QBrush(QColor(89, 210, 255, 255))
        brush27.setStyle(Qt.BrushStyle.SolidPattern)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush27)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush27)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush22)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush22)
        brush28 = QBrush(QColor(89, 210, 255, 128))
        brush28.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush28)
#endif
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush26)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush22)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush27)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush27)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush22)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush28)
#endif
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush25)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush22)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush27)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush27)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush22)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush28)
#endif
        self.cpu_label.setPalette(palette3)
        self.cpu_label.setFont(font)
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(820, 0, 67, 18))
        self.label_6.setFont(font6)
        self.ram_label = QLabel(self.frame_3)
        self.ram_label.setObjectName(u"ram_label")
        self.ram_label.setGeometry(QRect(890, 0, 81, 51))
        palette4 = QPalette()
        brush29 = QBrush(QColor(170, 0, 0, 255))
        brush29.setStyle(Qt.BrushStyle.SolidPattern)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush29)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush22)
        brush30 = QBrush(QColor(191, 0, 27, 255))
        brush30.setStyle(Qt.BrushStyle.SolidPattern)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush30)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush30)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush22)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush22)
        brush31 = QBrush(QColor(191, 0, 27, 128))
        brush31.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush31)
#endif
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush29)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush22)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush30)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush30)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush22)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush31)
#endif
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush25)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush22)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush30)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush30)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush22)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush31)
#endif
        self.ram_label.setPalette(palette4)
        self.ram_label.setFont(font)
        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(970, 0, 65, 18))
        self.label_9.setFont(font6)
        self.gpu_label = QLabel(self.frame_3)
        self.gpu_label.setObjectName(u"gpu_label")
        self.gpu_label.setGeometry(QRect(1040, 0, 91, 51))
        palette5 = QPalette()
        brush32 = QBrush(QColor(85, 170, 0, 255))
        brush32.setStyle(Qt.BrushStyle.SolidPattern)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush32)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush22)
        brush33 = QBrush(QColor(69, 255, 110, 255))
        brush33.setStyle(Qt.BrushStyle.SolidPattern)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush33)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush33)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush22)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush22)
        brush34 = QBrush(QColor(69, 255, 110, 128))
        brush34.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush34)
#endif
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush32)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush22)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush33)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush33)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush22)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush34)
#endif
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush25)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush22)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush33)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush33)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush22)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush22)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette5.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush34)
#endif
        self.gpu_label.setPalette(palette5)
        self.gpu_label.setFont(font)
        self.label_65 = QLabel(self.DatasetPage)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(10, 10, 701, 51))
        self.label_65.setFont(font4)
        self.stackedPanels.addWidget(self.DatasetPage)
        self.frame_4.raise_()
        self.frame_2.raise_()
        self.groupBox.raise_()
        self.frame_3.raise_()
        self.label_65.raise_()
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.label_52 = QLabel(self.page_10)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(10, 0, 671, 61))
        self.label_52.setFont(font4)
        self.actions_suspicion_level_combo_box = QComboBox(self.page_10)
        self.actions_suspicion_level_combo_box.addItem("")
        self.actions_suspicion_level_combo_box.addItem("")
        self.actions_suspicion_level_combo_box.addItem("")
        self.actions_suspicion_level_combo_box.addItem("")
        self.actions_suspicion_level_combo_box.addItem("")
        self.actions_suspicion_level_combo_box.addItem("")
        self.actions_suspicion_level_combo_box.addItem("")
        self.actions_suspicion_level_combo_box.addItem("")
        self.actions_suspicion_level_combo_box.addItem("")
        self.actions_suspicion_level_combo_box.addItem("")
        self.actions_suspicion_level_combo_box.addItem("")
        self.actions_suspicion_level_combo_box.setObjectName(u"actions_suspicion_level_combo_box")
        self.actions_suspicion_level_combo_box.setGeometry(QRect(40, 370, 311, 41))
        self.action_suspicion_level_table = QTableWidget(self.page_10)
        if (self.action_suspicion_level_table.columnCount() < 2):
            self.action_suspicion_level_table.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.action_suspicion_level_table.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.action_suspicion_level_table.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.action_suspicion_level_table.setObjectName(u"action_suspicion_level_table")
        self.action_suspicion_level_table.setGeometry(QRect(40, 90, 351, 241))
        self.action_suspicion_level_table.setTabKeyNavigation(True)
        self.action_suspicion_level_table.setProperty(u"showDropIndicator", True)
        self.action_suspicion_level_table.setWordWrap(True)
        self.action_suspicion_level_table.setRowCount(0)
        self.action_suspicion_level_table.setColumnCount(2)
        self.action_suspicion_level_table.horizontalHeader().setVisible(True)
        self.action_suspicion_level_table.horizontalHeader().setHighlightSections(True)
        self.action_suspicion_level_table.horizontalHeader().setStretchLastSection(False)
        self.action_suspicion_level_table.verticalHeader().setVisible(False)
        self.add_action_suspicion_level_button = QPushButton(self.page_10)
        self.add_action_suspicion_level_button.setObjectName(u"add_action_suspicion_level_button")
        self.add_action_suspicion_level_button.setGeometry(QRect(260, 450, 91, 41))
        self.label_26 = QLabel(self.page_10)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(30, 340, 71, 31))
        font17 = QFont()
        font17.setFamilies([u"Segoe UI"])
        font17.setBold(True)
        font17.setItalic(False)
        self.label_26.setFont(font17)
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.action_length_table = QTableWidget(self.page_10)
        if (self.action_length_table.columnCount() < 2):
            self.action_length_table.setColumnCount(2)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.action_length_table.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.action_length_table.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        self.action_length_table.setObjectName(u"action_length_table")
        self.action_length_table.setGeometry(QRect(420, 90, 361, 241))
        self.action_length_table.setTabKeyNavigation(True)
        self.action_length_table.setProperty(u"showDropIndicator", True)
        self.action_length_table.setWordWrap(True)
        self.action_length_table.setRowCount(0)
        self.action_length_table.setColumnCount(2)
        self.action_length_table.horizontalHeader().setVisible(True)
        self.action_length_table.horizontalHeader().setHighlightSections(True)
        self.action_length_table.horizontalHeader().setStretchLastSection(False)
        self.action_length_table.verticalHeader().setVisible(False)
        self.action_repitition_length_table = QTableWidget(self.page_10)
        if (self.action_repitition_length_table.columnCount() < 2):
            self.action_repitition_length_table.setColumnCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.action_repitition_length_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.action_repitition_length_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        self.action_repitition_length_table.setObjectName(u"action_repitition_length_table")
        self.action_repitition_length_table.setGeometry(QRect(800, 90, 341, 241))
        self.action_repitition_length_table.setTabKeyNavigation(True)
        self.action_repitition_length_table.setProperty(u"showDropIndicator", True)
        self.action_repitition_length_table.setWordWrap(True)
        self.action_repitition_length_table.setRowCount(0)
        self.action_repitition_length_table.setColumnCount(2)
        self.action_repitition_length_table.horizontalHeader().setVisible(True)
        self.action_repitition_length_table.horizontalHeader().setHighlightSections(True)
        self.action_repitition_length_table.horizontalHeader().setStretchLastSection(False)
        self.action_repitition_length_table.verticalHeader().setVisible(False)
        self.actions_length_combo_box = QComboBox(self.page_10)
        self.actions_length_combo_box.addItem("")
        self.actions_length_combo_box.addItem("")
        self.actions_length_combo_box.addItem("")
        self.actions_length_combo_box.addItem("")
        self.actions_length_combo_box.addItem("")
        self.actions_length_combo_box.addItem("")
        self.actions_length_combo_box.addItem("")
        self.actions_length_combo_box.addItem("")
        self.actions_length_combo_box.addItem("")
        self.actions_length_combo_box.addItem("")
        self.actions_length_combo_box.addItem("")
        self.actions_length_combo_box.setObjectName(u"actions_length_combo_box")
        self.actions_length_combo_box.setGeometry(QRect(420, 370, 301, 41))
        self.actions_repitiion_length_combo_box = QComboBox(self.page_10)
        self.actions_repitiion_length_combo_box.addItem("")
        self.actions_repitiion_length_combo_box.addItem("")
        self.actions_repitiion_length_combo_box.addItem("")
        self.actions_repitiion_length_combo_box.addItem("")
        self.actions_repitiion_length_combo_box.addItem("")
        self.actions_repitiion_length_combo_box.addItem("")
        self.actions_repitiion_length_combo_box.addItem("")
        self.actions_repitiion_length_combo_box.addItem("")
        self.actions_repitiion_length_combo_box.addItem("")
        self.actions_repitiion_length_combo_box.addItem("")
        self.actions_repitiion_length_combo_box.addItem("")
        self.actions_repitiion_length_combo_box.setObjectName(u"actions_repitiion_length_combo_box")
        self.actions_repitiion_length_combo_box.setGeometry(QRect(800, 370, 281, 41))
        self.suspicion_level_combo_box = QComboBox(self.page_10)
        self.suspicion_level_combo_box.addItem("")
        self.suspicion_level_combo_box.addItem("")
        self.suspicion_level_combo_box.addItem("")
        self.suspicion_level_combo_box.setObjectName(u"suspicion_level_combo_box")
        self.suspicion_level_combo_box.setGeometry(QRect(40, 450, 211, 41))
        self.label_69 = QLabel(self.page_10)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(30, 420, 131, 31))
        self.label_69.setFont(font17)
        self.label_69.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_28 = QLabel(self.page_10)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(410, 350, 71, 21))
        self.label_28.setFont(font17)
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_89 = QLabel(self.page_10)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setGeometry(QRect(790, 350, 71, 21))
        self.label_89.setFont(font17)
        self.label_89.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.action_length_line_edit = QLineEdit(self.page_10)
        self.action_length_line_edit.setObjectName(u"action_length_line_edit")
        self.action_length_line_edit.setGeometry(QRect(420, 450, 131, 41))
        self.label_90 = QLabel(self.page_10)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setGeometry(QRect(410, 420, 151, 31))
        self.label_90.setFont(font17)
        self.label_90.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.action_repitition_length_line_edit = QLineEdit(self.page_10)
        self.action_repitition_length_line_edit.setObjectName(u"action_repitition_length_line_edit")
        self.action_repitition_length_line_edit.setGeometry(QRect(800, 450, 121, 41))
        self.label_91 = QLabel(self.page_10)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setGeometry(QRect(790, 420, 211, 31))
        self.label_91.setFont(font17)
        self.label_91.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.add_action_length_button = QPushButton(self.page_10)
        self.add_action_length_button.setObjectName(u"add_action_length_button")
        self.add_action_length_button.setGeometry(QRect(630, 450, 91, 41))
        self.add_action_repitition_length_button = QPushButton(self.page_10)
        self.add_action_repitition_length_button.setObjectName(u"add_action_repitition_length_button")
        self.add_action_repitition_length_button.setGeometry(QRect(1000, 450, 81, 41))
        self.reset_tables_button = QPushButton(self.page_10)
        self.reset_tables_button.setObjectName(u"reset_tables_button")
        self.reset_tables_button.setGeometry(QRect(420, 600, 101, 41))
        self.clear_tables_button = QPushButton(self.page_10)
        self.clear_tables_button.setObjectName(u"clear_tables_button")
        self.clear_tables_button.setGeometry(QRect(590, 600, 101, 41))
        self.stackedPanels.addWidget(self.page_10)
        self.label_52.raise_()
        self.actions_suspicion_level_combo_box.raise_()
        self.action_suspicion_level_table.raise_()
        self.add_action_suspicion_level_button.raise_()
        self.label_26.raise_()
        self.action_length_table.raise_()
        self.action_repitition_length_table.raise_()
        self.suspicion_level_combo_box.raise_()
        self.label_69.raise_()
        self.label_28.raise_()
        self.label_89.raise_()
        self.actions_repitiion_length_combo_box.raise_()
        self.actions_length_combo_box.raise_()
        self.label_90.raise_()
        self.action_length_line_edit.raise_()
        self.label_91.raise_()
        self.action_repitition_length_line_edit.raise_()
        self.add_action_length_button.raise_()
        self.add_action_repitition_length_button.raise_()
        self.reset_tables_button.raise_()
        self.clear_tables_button.raise_()
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.label_54 = QLabel(self.page_13)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(10, 10, 271, 51))
        self.label_54.setFont(font4)
        self.slogan_about_us = QLabel(self.page_13)
        self.slogan_about_us.setObjectName(u"slogan_about_us")
        self.slogan_about_us.setGeometry(QRect(30, 80, 491, 160))
        font18 = QFont()
        font18.setFamilies([u"Bell MT"])
        font18.setWeight(QFont.Medium)
        font18.setItalic(True)
        self.slogan_about_us.setFont(font18)
        self.slogan_about_us.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textEdit = QTextEdit(self.page_13)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(40, 250, 481, 281))
        self.Back_to_Home_button_from_about_us = QPushButton(self.page_13)
        self.Back_to_Home_button_from_about_us.setObjectName(u"Back_to_Home_button_from_about_us")
        self.Back_to_Home_button_from_about_us.setGeometry(QRect(930, 580, 181, 51))
        self.Back_to_Home_button_from_about_us.setFont(font6)
        self.Back_to_Home_button_from_about_us.setIcon(icon9)
        self.Back_to_Home_button_from_about_us.setIconSize(QSize(25, 25))
        self.label_68 = QLabel(self.page_13)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(290, -5, 991, 561))
        self.label_68.setPixmap(QPixmap(u":/icons/about us.png"))
        self.label_68.setScaledContents(True)
        self.label_83 = QLabel(self.page_13)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setGeometry(QRect(550, 210, 711, 371))
        self.label_83.setPixmap(QPixmap(u":/icons/Untitled design (5).png"))
        self.label_83.setScaledContents(True)
        self.stackedPanels.addWidget(self.page_13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1340, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.actionNew_Project)
        self.menuFile.addAction(self.actionImport_Video)
        self.menuFile.addAction(self.actionExport_Data_Analytics_Results)
        self.menuFile.addAction(self.actionExit_Application)
        self.menuView.addAction(self.actionAI_Analytics_Results)
        self.menuView.addAction(self.actionAdvanced_Analytics_Results)
        self.menuView.addAction(self.actionTutorial)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionAbout_Us_Panel)
        self.menuView.addAction(self.actionCreate_Dataset)
        self.menuView.addAction(self.actionCalibrate_Camera)

        self.retranslateUi(MainWindow)

        self.stackedPanels.setCurrentIndex(3)
        self.stacked_panels_ai_analytics.setCurrentIndex(0)
        self.visualization_stackedpanels_3.setCurrentIndex(0)
        self.heatmap_actions_ai_analytics_combo_box.setCurrentIndex(0)
        self.ai_analytics_line_graph_combo_box.setCurrentIndex(-1)
        self.ai_analytics_visualization_combo_box.setCurrentIndex(0)
        self.stacked_advanced_analytics.setCurrentIndex(0)
        self.visualization_stackedpanels_2.setCurrentIndex(0)
        self.heatmap_actions_advanced_analytics_combo_box.setCurrentIndex(0)
        self.advanced_analytics_actions_combo_box.setCurrentIndex(-1)
        self.advanced_analytics_visualization_combo_box.setCurrentIndex(0)
        self.document_export_combo_box.setCurrentIndex(-1)
        self.actions_suspicion_level_combo_box.setCurrentIndex(0)
        self.actions_length_combo_box.setCurrentIndex(0)
        self.actions_repitiion_length_combo_box.setCurrentIndex(0)
        self.suspicion_level_combo_box.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Action Coding Engine (ACE) - Prototype Version", None))
        self.actionTutorial_Tab.setText(QCoreApplication.translate("MainWindow", u"Tutorial Tab", None))
        self.actionAbout_Us.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.actionCreate_Dataset_Tab.setText(QCoreApplication.translate("MainWindow", u"Create Dataset Tab", None))
        self.actionHome.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"Import Video", None))
        self.actionAI_Analytics.setText(QCoreApplication.translate("MainWindow", u"AI Analytics", None))
        self.actionAdvanced_Analytics.setText(QCoreApplication.translate("MainWindow", u"Advanced Analytics", None))
        self.actionExport_Data.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionImport_Video.setText(QCoreApplication.translate("MainWindow", u"Import Video", None))
        self.actionExit_Application.setText(QCoreApplication.translate("MainWindow", u"Exit Application", None))
        self.actionAI_Analytics_Tab.setText(QCoreApplication.translate("MainWindow", u"AI Analytics", None))
        self.actionAdvanced_Analytics_2.setText(QCoreApplication.translate("MainWindow", u"Advanced Analytics", None))
        self.actionAI_Analytics_Results.setText(QCoreApplication.translate("MainWindow", u"AI Analytics Results", None))
        self.actionAdvanced_Analytics_Results.setText(QCoreApplication.translate("MainWindow", u"Advanced Analytics Results", None))
        self.actionExport_Data_Analytics_Results.setText(QCoreApplication.translate("MainWindow", u"Export Data Analytics Results", None))
        self.actionAbout_Us_Panel.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.actionTutorial.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.actionNew_Project.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.actionCreate_Dataset.setText(QCoreApplication.translate("MainWindow", u"Create Dataset", None))
        self.actionCalibrate_Camera.setText(QCoreApplication.translate("MainWindow", u"Calibrate Criteria", None))
        self.ProjectName.setText(QCoreApplication.translate("MainWindow", u"Action Coding\n"
"Engine (ACE)", None))
        self.Home_button.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.Import_button.setText(QCoreApplication.translate("MainWindow", u"IMPORT\n"
"VIDEO", None))
        self.Exit_button.setText(QCoreApplication.translate("MainWindow", u"EXIT", None))
        self.Advanced_analytics_button.setText(QCoreApplication.translate("MainWindow", u"HEAD AND ARMS\n"
"VISUALIZATIONS", None))
        self.Tutorial_button.setText(QCoreApplication.translate("MainWindow", u"TUTORIAL", None))
        self.Export_file_button.setText(QCoreApplication.translate("MainWindow", u"EXPORT DATA", None))
        self.AI_analytics_button.setText(QCoreApplication.translate("MainWindow", u"AI\n"
"VISUALIZATIONS", None))
        self.logo.setText("")
        self.Homepage_label.setText(QCoreApplication.translate("MainWindow", u"Action Coding Engine", None))
        self.slogan2.setText(QCoreApplication.translate("MainWindow", u"E  v  e  r  y    A  c  t  i  o  n,", None))
        self.slogan3.setText(QCoreApplication.translate("MainWindow", u"E  v  e  r  y    D  e  t  a  i  l!", None))
        self.label_14.setText("")
        self.label_84.setText("")
        self.label_85.setText("")
        self.small_intro.setText(QCoreApplication.translate("MainWindow", u"\u2023 Revolutionize your examination analysis with\n"
"the Action Coding Engine!\n"
"\n"
"\u2023 Seamlessly track, analyze, and visualize student\n"
"behavior from recorded footage, providing instant\n"
"insights into engagement and actions.\n"
"\n"
"\u2023 Explore detailed heatmaps and charts that bring\n"
"clarity to student behavior patterns, all at the touch\n"
"of a button.", None))
        self.label_86.setText("")
        self.label_87.setText("")
        self.label_88.setText("")
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START!", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Enter Session Name: *", None))
        self.slogan1.setText(QCoreApplication.translate("MainWindow", u"Import,        Analyze,         Visualize!", None))
        self.status_label_front.setText(QCoreApplication.translate("MainWindow", u"[ IMPORT A VIDEO ]", None))
        self.import_video_button_front.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.videoDirectory_front.setText(QCoreApplication.translate("MainWindow", u"Import a center view video file to be analyzed.", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Front Video File Location:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Center Video File Location:", None))
        self.videoDirectory_center.setText(QCoreApplication.translate("MainWindow", u"Import a center view video file to be analyzed.", None))
        self.status_label_center.setText(QCoreApplication.translate("MainWindow", u"[ IMPORT A VIDEO ]", None))
        self.import_video_button_center.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.play_pause_button_video_preview.setText(QCoreApplication.translate("MainWindow", u"PLAY PREVIEW", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Time Elapsed:", None))
        self.time_elapsed_label_front.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.time_elapsed_label_center.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Time Elapsed:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Time:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Video Preview [FRONT]", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Video Preview [CENTER]", None))
        self.day_label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Session Name:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.session_name_label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"UPLOAD AN\n"
"EXAMINATION FOOTAGE", None))
        self.video_preview_label_front.setText(QCoreApplication.translate("MainWindow", u"Import a video to see preview", None))
        self.video_preview_label_center.setText(QCoreApplication.translate("MainWindow", u"Import a video to see preview", None))
        self.front_preview_video_keypoints_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.front_preview_video_bounding_box_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.center_preview_video_bounding_box_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.center_preview_video_keypoints_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.front_preview_video_dark_mode_check_box.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.center_preview_video_dark_mode_check_box.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.video_preview_label_ai_analytics_center.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.video_preview_label_ai_analytics_front.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.heatmap_ai_analytics_label.setText(QCoreApplication.translate("MainWindow", u"Heatmap Visualization will be presented here.", None))
        self.heatmap_actions_ai_analytics_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"ALL ACTIONS", None))
        self.heatmap_actions_ai_analytics_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"LEFT ARM EXTENDING SIDEWARDS", None))
        self.heatmap_actions_ai_analytics_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"RIGHT ARM EXTENDING SIDEWARDS", None))
        self.heatmap_actions_ai_analytics_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"FACING DOWNWARDS", None))
        self.heatmap_actions_ai_analytics_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"FACING FORWARD", None))
        self.heatmap_actions_ai_analytics_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"FACING LEFT", None))
        self.heatmap_actions_ai_analytics_combo_box.setItemText(6, QCoreApplication.translate("MainWindow", u"FACING RIGHT", None))
        self.heatmap_actions_ai_analytics_combo_box.setItemText(7, QCoreApplication.translate("MainWindow", u"SITTING", None))
        self.heatmap_actions_ai_analytics_combo_box.setItemText(8, QCoreApplication.translate("MainWindow", u"STANDING", None))

        self.heatmap_actions_ai_analytics_combo_box.setCurrentText(QCoreApplication.translate("MainWindow", u"ALL ACTIONS", None))
        self.view_button_ai_analytics_heatmap.setText(QCoreApplication.translate("MainWindow", u"VIEW", None))
        self.visualization1_label_3.setText(QCoreApplication.translate("MainWindow", u"Visualization1 will be here", None))
        self.heatmap_present_label_6.setText(QCoreApplication.translate("MainWindow", u"Visualization2 is here", None))
        self.play_pause_button_ai_analytics_heatmap.setText(QCoreApplication.translate("MainWindow", u"PLAY PREVIEW", None))
        self.CenterPlacement_label_3.setText(QCoreApplication.translate("MainWindow", u" Center Video Placement", None))
        self.keypoints_check_box_ai_analytics_center.setText(QCoreApplication.translate("MainWindow", u"Keypoints Only", None))
        self.bounding_box_check_box_ai_analytics_center.setText(QCoreApplication.translate("MainWindow", u"Bounding Box", None))
        self.bounding_box_check_box_ai_analytics_front.setText(QCoreApplication.translate("MainWindow", u"Bounding Box", None))
        self.keypoints_check_box_ai_analytics_front.setText(QCoreApplication.translate("MainWindow", u"Keypoints Only", None))
        self.FrontPlacement_label_3.setText(QCoreApplication.translate("MainWindow", u"Front Video Placement", None))
        self.dark_mode_check_box_ai_analytics_center.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.dark_mode_check_box_ai_analytics_front.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.identify_suspicious_check_box_heatmap_ai_analytics.setText(QCoreApplication.translate("MainWindow", u"Suspicious\n"
"Movements", None))
        self.ai_analytics_preview_front.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.ai_analytics_preview_center.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.play_pause_button__ai_analytics_line_graph.setText(QCoreApplication.translate("MainWindow", u"PLAY PREVIEW", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Left Arm Extending\n"
"Sidewards", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Right Arm Extending\n"
"Sidewards", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Facing Downwards", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Facing Forward", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Facing Left", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Facing Right", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Sitting", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Standing", None))
        self.front_preview_video_bounding_box_ai_analytics_line_graph_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.front_preview_video_keypoints_ai_analytics_line_graph_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Video Preview [FRONT]", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Video Preview [CENTER]", None))
        self.center_preview_video_bounding_box_ai_analytics_line_graph_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.center_preview_video_keypoints_ai_analytics_line_graph_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.ai_analytics_count_standing.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ai_analytics_count_sitting.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ai_analytics_count_facing_right.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ai_analytics_count_facing_left.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ai_analytics_count_facing_forward.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ai_analytics_count_facing_downwards.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ai_analytics_count_right_arm_extending_sidewards.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ai_analytics_count_left_arm_extending_sidewards.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"# of Detected Students", None))
        self.ai_analytics_count_students.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Realtime Data Counts", None))
        self.identify_suspicious_check_box_line_graph_ai_analytics.setText(QCoreApplication.translate("MainWindow", u"Suspicious\n"
"Movements", None))
        self.play_pause_button_ai_analytics_table_event_logs.setText(QCoreApplication.translate("MainWindow", u"PLAY PREVIEW", None))
        self.ai_analytics_table_event_logs_preview_front.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.ai_analytics_table_event_logs_preview_center.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.TimeLabel.setText(QCoreApplication.translate("MainWindow", u"8:10s - 11:39s", None))
        self.TimeLabel_2.setText(QCoreApplication.translate("MainWindow", u"Time Range:", None))
        self.center_preview_video_keypoints_ai_analytics_event_logs_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.center_preview_video_bounding_box_ai_analytics_event_logs_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Video Preview [CENTER]", None))
        self.front_preview_video_keypoints_ai_analytics_event_logs_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.front_preview_video_bounding_box_ai_analytics_event_logs_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Video Preview [CENTER]", None))
        ___qtablewidgetitem = self.ai_analytics_event_summary_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Time Range", None));
        ___qtablewidgetitem1 = self.ai_analytics_event_summary_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"AI Summary Log", None));
        self.front_preview_video_bounding_box_ai_analytics_event_summary_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.center_preview_video_keypoints_ai_analytics_event_summary_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.ai_analytics_chunk_summary_preview_front.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Video Preview [CENTER]", None))
        self.center_preview_video_bounding_box_ai_analytics_event_summary_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.ai_analytics_chunk_summary_preview_center.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Video Preview [CENTER]", None))
        self.front_preview_video_keypoints_ai_analytics_event_summary_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.ai_analytics_event_summary_play_pause_button.setText(QCoreApplication.translate("MainWindow", u"PLAY PREVIEW", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Logs Interval", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"In seconds:", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Summary Data is logged every:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"In minutes:", None))
        self.interval_time_label.setText(QCoreApplication.translate("MainWindow", u"0 mins  2 secs", None))
        self.ai_analytics_label.setText(QCoreApplication.translate("MainWindow", u"AI VISUALIZATIONS - HEATMAP", None))
        self.ai_analytics_visualization_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Heatmap", None))
        self.ai_analytics_visualization_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Line Graph", None))
        self.ai_analytics_visualization_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Event Logs Tables", None))
        self.ai_analytics_visualization_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Event Summary", None))

        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Current\n"
"Visualization:", None))
        self.advanced_analytics_heatmap_preview_center.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.advanced_analytics_heatmap_preview_front.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.heatmap_actions_advanced_analytics_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"ALL ACTIONS", None))
        self.heatmap_actions_advanced_analytics_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"FACING DOWNWARDS", None))
        self.heatmap_actions_advanced_analytics_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"FACING LEFT", None))
        self.heatmap_actions_advanced_analytics_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"FACING RIGHT", None))
        self.heatmap_actions_advanced_analytics_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"FACING FORWARD", None))
        self.heatmap_actions_advanced_analytics_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"LEFT ARM NEUTRAL (RESTING)", None))
        self.heatmap_actions_advanced_analytics_combo_box.setItemText(6, QCoreApplication.translate("MainWindow", u"LEFT ARM EXTENDING SIDEWARDS", None))
        self.heatmap_actions_advanced_analytics_combo_box.setItemText(7, QCoreApplication.translate("MainWindow", u"LEFT ARM UNKNOWN", None))
        self.heatmap_actions_advanced_analytics_combo_box.setItemText(8, QCoreApplication.translate("MainWindow", u"RIGHT ARM NEUTRAL (RESTING)", None))
        self.heatmap_actions_advanced_analytics_combo_box.setItemText(9, QCoreApplication.translate("MainWindow", u"RIGHT ARM EXTENDING SIDEWARDS", None))
        self.heatmap_actions_advanced_analytics_combo_box.setItemText(10, QCoreApplication.translate("MainWindow", u"RIGHT ARM UNKNOWN", None))

        self.heatmap_actions_advanced_analytics_combo_box.setCurrentText(QCoreApplication.translate("MainWindow", u"ALL ACTIONS", None))
        self.view_button_advanced_analytics_heatmap.setText(QCoreApplication.translate("MainWindow", u"VIEW", None))
        self.heatmap_advanced_analytics_label.setText(QCoreApplication.translate("MainWindow", u"Heatmap Visualization will be presented here.", None))
        self.visualization1_label_2.setText(QCoreApplication.translate("MainWindow", u"Visualization1 will be here", None))
        self.heatmap_present_label_4.setText(QCoreApplication.translate("MainWindow", u"Visualization2 is here", None))
        self.CenterPlacement_label_2.setText(QCoreApplication.translate("MainWindow", u"Center Video Placement", None))
        self.FrontPlacement_label_2.setText(QCoreApplication.translate("MainWindow", u"Front Video Placement", None))
        self.play_pause_button_advanced_analytics_heatmap.setText(QCoreApplication.translate("MainWindow", u"PLAY PREVIEW", None))
        self.dark_mode_check_box_advanced_analytics_center.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.keypoints_check_box_advanced_analytics_center.setText(QCoreApplication.translate("MainWindow", u"Keypoints Only", None))
        self.bounding_box_check_box_advanced_analytics_center.setText(QCoreApplication.translate("MainWindow", u"Bounding Box", None))
        self.bounding_box_check_box_advanced_analytics_front.setText(QCoreApplication.translate("MainWindow", u"Bounding Box", None))
        self.dark_mode_check_box_advanced_analytics_front.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.keypoints_check_box_advanced_analytics_front.setText(QCoreApplication.translate("MainWindow", u"Keypoints Only", None))
        self.identify_suspicious_check_box_heatmap_advanced_analytics.setText(QCoreApplication.translate("MainWindow", u"Suspicious\n"
"Movements", None))
        self.adv_analytics_preview_line_graph_front.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.adv_analytics_preview_line_graph_center.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.play_pause_button_advanced_analytics_line_graph.setText(QCoreApplication.translate("MainWindow", u"PLAY PREVIEW", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Left Arm Extending\n"
"Sidewards", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Facing Left", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Facing Forward", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Facing Right", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Facing Downwards", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Right Arm Extending\n"
"Sidewards", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Left Arm Neutral", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Left Arm Unknown", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Right Arm Neutral", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Right Arm Unknown", None))
        self.front_preview_video_bounding_box_advanced_analytics_line_chart_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Video Preview [CENTER]", None))
        self.center_preview_video_bounding_box_advanced_analytics_line_chart_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Video Preview [FRONT]", None))
        self.center_preview_video_keypoints_advanced_analytics_line_chart_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.front_preview_video_keypoints_advanced_analytics_line_chart_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.advanced_analytics_count_facing_left.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.advanced_analytics_count_left_arm_extending_sidewards.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.advanced_analytics_count_facing_right.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.advanced_analytics_count_right_arm_extending_sidewards.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.advanced_analytics_count_facing_forward.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.advanced_analytics_count_facing_downwards.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"# of Students Detected", None))
        self.advanced_analytics_count_students.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.advanced_analytics_count_right_arm_unknown.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.advanced_analytics_count_right_arm_neutral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.advanced_analytics_count_left_arm_unknown.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.advanced_analytics_count_left_arm_neutral.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.identify_suspicious_check_box_line_graph_advanced_analytics.setText(QCoreApplication.translate("MainWindow", u"Suspicious\n"
"Movements", None))
        self.play_pause_button_advanced_analytics_table_event_logs.setText(QCoreApplication.translate("MainWindow", u"PLAY PREVIEW", None))
        self.adv_analytics_preview_event_logs_table_front.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.adv_analytics_preview_event_logs_table_center.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.front_preview_video_bounding_box_advanced_analytics_event_logs_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Video Preview [CENTER]", None))
        self.center_preview_video_bounding_box_advanced_analytics_event_logs_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Video Preview [CENTER]", None))
        self.center_preview_video_keypoints_advanced_analytics_event_logs_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.front_preview_video_keypoints_advanced_analytics_event_logs_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Summary Data is logged every:", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"In minutes:", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Logs Interval", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"In seconds:", None))
        self.interval_time_label_advanced_analytics.setText(QCoreApplication.translate("MainWindow", u"0 mins  2 secs", None))
        self.front_preview_video_bounding_box_advanced_analytics_event_summary_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.advanced_analytics_chunk_summary_preview_front.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Video Preview [CENTER]", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Video Preview [CENTER]", None))
        ___qtablewidgetitem2 = self.advanced_analytics_event_summary_table.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Time Range", None));
        ___qtablewidgetitem3 = self.advanced_analytics_event_summary_table.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"AI Summary Log", None));
        self.advanced_analytics_event_summary_play_pause_button.setText(QCoreApplication.translate("MainWindow", u"PLAY PREVIEW", None))
        self.center_preview_video_bounding_box_advanced_analytics_event_summary_check_box.setText(QCoreApplication.translate("MainWindow", u"Bounding Boxes", None))
        self.advanced_analytics_chunk_summary_preview_center.setText(QCoreApplication.translate("MainWindow", u"Import an Examination Footage First", None))
        self.center_preview_video_keypoints_advanced_analytics_event_summary_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.front_preview_video_keypoints_advanced_analytics_event_summary_check_box.setText(QCoreApplication.translate("MainWindow", u"Keypoints", None))
        self.advanced_analytics_visualization_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Heatmap", None))
        self.advanced_analytics_visualization_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Line Graph", None))
        self.advanced_analytics_visualization_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Event Logs Table", None))
        self.advanced_analytics_visualization_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Events Summary", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"HEAD & ARM VISUALIZATIONS", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Current\n"
"Visualization:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"EXPORT DATA ANALYTICS", None))
        self.generate_document_report.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Generate Reports:", None))
        self.ai_analytics_export_radio_button.setText(QCoreApplication.translate("MainWindow", u"AI Analytics", None))
        self.advanced_analytics_export_radio_button.setText(QCoreApplication.translate("MainWindow", u"Advanced Analytics", None))
        self.front_video_only_radio_button.setText(QCoreApplication.translate("MainWindow", u"Front Video Only", None))
        self.center_video_only_radio_button.setText(QCoreApplication.translate("MainWindow", u"Center Video Only", None))
        self.both_front_and_center_video_button.setText(QCoreApplication.translate("MainWindow", u"Both Front and Center Video", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"MEDIA SETTINGS", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"CAMERA ANGLES", None))
        self.add_keypoints_check_box.setText(QCoreApplication.translate("MainWindow", u"Add Keypoints", None))
        self.add_bounding_box_check_box.setText(QCoreApplication.translate("MainWindow", u"Add Bounding Box", None))
        self.suspicious_movements_option_export.setText(QCoreApplication.translate("MainWindow", u"Suspicious Movements", None))
        self.document_export_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Full Report (.pdf)", None))
        self.document_export_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Detections Video (.mp4)", None))
        self.document_export_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Heatmap Video (.mp4)", None))

        self.document_export_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select document type to export...", None))
        self.send_to_email_button.setText(QCoreApplication.translate("MainWindow", u"Export to Send Email", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Analyzation Tutorial", None))
        self.stepbystepTutorial_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI','sans-serif'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:20pt;\">Lorem ipsum odor amet, consectetuer adipiscing elit. Per nibh massa magna potenti euismod vestibulum non. Elementum eros nascetur id felis proin proin fames. Massa potenti ultrices facilisi fames hac. Eleifend amet nam habitasse elementum inceptos hac habitasse posuere platea. Sed hendrerit inceptos lacinia arcu, mattis habitasse t"
                        "incidunt. Vel mauris lacinia dis lacinia auctor tellus integer elementum. Tempus faucibus mattis nisi consequat at habitasse. Torquent iaculis fringilla parturient dolor facilisi ad.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Dataset Tutorial", None))
        self.Back_to_Home_button.setText(QCoreApplication.translate("MainWindow", u"Back to Home", None))
        self.stepbystepTutorial_text_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI','sans-serif'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:20pt;\">Lorem ipsum odor amet, consectetuer adipiscing elit. Per nibh massa magna potenti euismod vestibulum non. Elementum eros nascetur id felis proin proin fames. Massa potenti ultrices facilisi fames hac. Eleifend amet nam habitasse elementum inceptos hac habitasse posuere platea. Sed hendrerit inceptos lacinia arcu, mattis habitasse t"
                        "incidunt. Vel mauris lacinia dis lacinia auctor tellus integer elementum. Tempus faucibus mattis nisi consequat at habitasse. Torquent iaculis fringilla parturient dolor facilisi ad.</span></p></body></html>", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"TUTORIAL", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"NOT RECORDING", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.camera_feed.setText(QCoreApplication.translate("MainWindow", u"Camera Feed will show here", None))
        self.white_frame_feed.setText(QCoreApplication.translate("MainWindow", u"Body Pose Key Points will show here", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Camera Feed", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Key Points Visualization", None))
        self.showCameraLandmarksChkBox.setText(QCoreApplication.translate("MainWindow", u"Show Body Landmarks", None))
        self.show_whiteframe_boundingbox.setText(QCoreApplication.translate("MainWindow", u"Show Bounding Boxes", None))
        self.showCameraBoundingBoxChkBox.setText(QCoreApplication.translate("MainWindow", u"Show Bounding Box", None))
        self.show_skeleton_camera.setText(QCoreApplication.translate("MainWindow", u"Show in Skeleton", None))
        self.darkMode_whiteframe.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.show_skeleton_white_frame.setText(QCoreApplication.translate("MainWindow", u"Show in Skeleton", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"ACTION:", None))
        self.refresh_button.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.recording_button.setText(QCoreApplication.translate("MainWindow", u"START\n"
"RECORDING", None))
        self.add_action_button.setText(QCoreApplication.translate("MainWindow", u"Add Action", None))
        self.delete_action_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Dataset Details", None))
        self.interval_label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Folder Location", None))
        self.refresh_action_list.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.sequence_label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"No. of Frames per Video", None))
        self.browseButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Break Interval Length", None))
        self.label_Camera.setText(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.openCamera.setText(QCoreApplication.translate("MainWindow", u"Open Camera", None))
        self.closeCamera.setText(QCoreApplication.translate("MainWindow", u"Close Camera", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"FPS:", None))
        self.fps_label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CPU Usage", None))
        self.cpu_label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"RAM Usage", None))
        self.ram_label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"GPU Usage", None))
        self.gpu_label.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"DATASET COLLECTION", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Suspiciousness Criteria Calibrator", None))
        self.actions_suspicion_level_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"SITTING", None))
        self.actions_suspicion_level_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"STANDING", None))
        self.actions_suspicion_level_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"LEFT ARM EXTENDING SIDEWARDS", None))
        self.actions_suspicion_level_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"LEFT ARM NEUTRAL (RESTING)", None))
        self.actions_suspicion_level_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"LEFT ARM UNKNOWN", None))
        self.actions_suspicion_level_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"RIGHT ARM EXTENDING SIDEWARDS", None))
        self.actions_suspicion_level_combo_box.setItemText(6, QCoreApplication.translate("MainWindow", u"RIGHT ARM NEUTRAL (RESTING)", None))
        self.actions_suspicion_level_combo_box.setItemText(7, QCoreApplication.translate("MainWindow", u"RIGHT ARM UNKNOWN", None))
        self.actions_suspicion_level_combo_box.setItemText(8, QCoreApplication.translate("MainWindow", u"FACING LEFT", None))
        self.actions_suspicion_level_combo_box.setItemText(9, QCoreApplication.translate("MainWindow", u"FACING FORWARDS", None))
        self.actions_suspicion_level_combo_box.setItemText(10, QCoreApplication.translate("MainWindow", u"FACING DOWNWARDS", None))

        self.actions_suspicion_level_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose an action...", None))
        ___qtablewidgetitem4 = self.action_suspicion_level_table.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Action Name", None));
        ___qtablewidgetitem5 = self.action_suspicion_level_table.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Suspicion Level", None));
        self.add_action_suspicion_level_button.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Action", None))
        ___qtablewidgetitem6 = self.action_length_table.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Action Name", None));
        ___qtablewidgetitem7 = self.action_length_table.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Length (s)", None));
        ___qtablewidgetitem8 = self.action_repitition_length_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Action Name", None));
        ___qtablewidgetitem9 = self.action_repitition_length_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Repitition Count", None));
        self.actions_length_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"SITTING", None))
        self.actions_length_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"STANDING", None))
        self.actions_length_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"LEFT ARM EXTENDING SIDEWARDS", None))
        self.actions_length_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"LEFT ARM NEUTRAL (RESTING)", None))
        self.actions_length_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"LEFT ARM UNKNOWN", None))
        self.actions_length_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"RIGHT ARM EXTENDING SIDEWARDS", None))
        self.actions_length_combo_box.setItemText(6, QCoreApplication.translate("MainWindow", u"RIGHT ARM NEUTRAL (RESTING)", None))
        self.actions_length_combo_box.setItemText(7, QCoreApplication.translate("MainWindow", u"RIGHT ARM UNKNOWN", None))
        self.actions_length_combo_box.setItemText(8, QCoreApplication.translate("MainWindow", u"FACING LEFT", None))
        self.actions_length_combo_box.setItemText(9, QCoreApplication.translate("MainWindow", u"FACING FORWARDS", None))
        self.actions_length_combo_box.setItemText(10, QCoreApplication.translate("MainWindow", u"FACING DOWNWARDS", None))

        self.actions_length_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose an action...", None))
        self.actions_repitiion_length_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"SITTING", None))
        self.actions_repitiion_length_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"STANDING", None))
        self.actions_repitiion_length_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"LEFT ARM EXTENDING SIDEWARDS", None))
        self.actions_repitiion_length_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"LEFT ARM NEUTRAL (RESTING)", None))
        self.actions_repitiion_length_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"LEFT ARM UNKNOWN", None))
        self.actions_repitiion_length_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"RIGHT ARM EXTENDING SIDEWARDS", None))
        self.actions_repitiion_length_combo_box.setItemText(6, QCoreApplication.translate("MainWindow", u"RIGHT ARM NEUTRAL (RESTING)", None))
        self.actions_repitiion_length_combo_box.setItemText(7, QCoreApplication.translate("MainWindow", u"RIGHT ARM UNKNOWN", None))
        self.actions_repitiion_length_combo_box.setItemText(8, QCoreApplication.translate("MainWindow", u"FACING LEFT", None))
        self.actions_repitiion_length_combo_box.setItemText(9, QCoreApplication.translate("MainWindow", u"FACING FORWARDS", None))
        self.actions_repitiion_length_combo_box.setItemText(10, QCoreApplication.translate("MainWindow", u"FACING DOWNWARDS", None))

        self.actions_repitiion_length_combo_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose an action...", None))
        self.suspicion_level_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"HIGHLY SUSPICIOUS", None))
        self.suspicion_level_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"MODERATELY SUSPICIOUS", None))
        self.suspicion_level_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"NON-SUSPICIOUS", None))

        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Suspicion Level", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Action", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Action", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Action's Length (s)", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Action's Repitition Length (s)", None))
        self.add_action_length_button.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.add_action_repitition_length_button.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.reset_tables_button.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.clear_tables_button.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"ABOUT US", None))
        self.slogan_about_us.setText(QCoreApplication.translate("MainWindow", u"We turn student exam behavior \n"
"into data-driven insight.", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI','sans-serif'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">	We are a research team developing software that digitizes behavioral coding through action recognition models. By analyzing in-person exam footage, our tool captures and classifies student behaviors to offer psychological and educational insights. Through visualization features like timelines, logs, and heatmaps, we help bring structure and clarity to cl"
                        "assroom observation.</span></p></body></html>", None))
        self.Back_to_Home_button_from_about_us.setText(QCoreApplication.translate("MainWindow", u"Back to Home", None))
        self.label_68.setText("")
        self.label_83.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

