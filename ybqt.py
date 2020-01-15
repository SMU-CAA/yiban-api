#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import re
import json
import time
import getopt
import random
import requests
import traceback
from ybapi import ybvote, ybtopic, yblogin
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, QtNetwork
from ybqtmainui import Ui_mainWindow
from ybqtloginui import Ui_LoginWindow

class MyThread(QtCore.QThread):

    def __init__(self, token, clearance, captcha, add_vote_count, vote_control_count, vote_reply_count, add_topic_count, topic_control_count, topic_reply_count, vote, vote_up, vote_reply, topic_up, topic_reply, url, waitime):
        super(MyThread, self).__init__()
        self.token = dict(yiban_user_token=token, _ydclearance=clearance)
        self.add_vote_count = add_vote_count
        self.vote_control_count = vote_control_count
        self.vote_reply_count = vote_reply_count
        self.add_topic_count = add_topic_count
        self.topic_control_count = topic_control_count
        self.topic_reply_count = topic_reply_count
        self.vote = vote
        self.vote_up = vote_up
        self.vote_reply = vote_reply
        self.topic_up = topic_up
        self.topic_reply = topic_reply
        self.url = url
        self.waitime = waitime

    def getURL(self):
        Get_Url = r.get(self.url, timeout=10)
        return str(Get_Url.text)

    def wait(self):
        try:
            self.getEGPA()
        except:
            pass
        finally:
            time.sleep(float(self.waitime))

    def fprint(self, string, dlevel=0, num=0):
        dbglevel = {
            0: "",
            1: "I: ",
            2: "W: ",
            3: "E: "
        }
        if num > 0:
            number = " #" + str(num + 1)
        else:
            number = ""
        return dbglevel.get(dlevel) + string + number

    def login(self):
        try:
            self.sig.emit(self.fprint("易班 Token: " + self.token['yiban_user_token'], dlevel=1))
            self.info = yblogin.getInfo(self.token)
            self.group_id = self.info["group_id"]
            self.puid = self.info["puid"]
            self.channel_id = self.info["channel_id"]
            self.actor_id = self.info["actor_id"]
            self.nick = self.info["nick"]
            self.sig.emit(self.fprint(self.nick + ": 登陆成功", dlevel=1))
            return 0
        except:
            self.sig.emit(self.fprint("无法连接服务器或 Token 错误，请重新使用账号/密码登录。" + traceback.format_exc(), dlevel=3))
            return 2
        finally:
            self.wait()

    def getEGPA(self):
        try:
            Get_EGPA = r.get(yblogin.BASEURL + "newgroup/indexPub/group_id/" +
                             self.group_id + "/puid/" + self.puid, cookies=self.token, headers=yblogin.header, timeout=10)
            EGPA = re.search(r"EGPA：[0-9\.]*", Get_EGPA.text)
            self.egpasig.emit(EGPA.group())
        except:
            self.egpasig.emit("无法连接服务器")

    def runVote(self):
        try:
            self.prog = 50 / (int(self.add_vote_count) + int(self.vote_control_count)
                          * (self.vote / 2 + self.vote / 2 + self.vote_reply / 2 * int(self.vote_reply_count)))
        except:
            self.prog = 0
        for i in range(0, int(self.add_vote_count)):
            try:
                text = self.getURL()
                response = ybvote.vote(
                    self.token,
                    self.puid,
                    self.group_id
                ).add(
                    text,
                    text,
                    text,
                    text
                )
                self.sig.emit(self.fprint("添加投票" + response, dlevel=1, num=i))
            except:
                self.sig.emit(self.fprint("添加投票时未获取到的错误" + traceback.format_exc(), dlevel=2, num=i))
            finally:
                self.pro = self.pro + self.prog
                self.prosig.emit(int(self.pro))
                self.wait()
        voteget = []
        for i in range(0, int(self.vote_control_count)):
            try:
                votevote = ybvote.vote(
                    self.token,
                    self.puid,
                    self.group_id
                )
                if not voteget:
                    voteget = votevote.get(self.vote_control_count)
                self.vote_id = voteget[i]["id"]
                votego = ybvote.go(
                    self.token,
                    self.puid,
                    self.group_id,
                    self.actor_id,
                    self.vote_id,
                    isOrganization=0,
                    ispublic=0
                )
                if self.vote:
                    try:
                        response = votego.vote(auto=True)
                        self.sig.emit(self.fprint(
                            "参与投票" + response, dlevel=1, num=i))
                    except:
                        self.sig.emit(self.fprint(
                            "参与投票时未获取到的错误" + traceback.format_exc(), dlevel=2, num=i))
                    finally:
                        self.pro = self.pro + self.prog
                        self.prosig.emit(int(self.pro))
                        self.wait()
                if self.vote_up:
                    try:
                        response = votego.up()
                        self.sig.emit(self.fprint(
                            "点赞投票" + response, dlevel=1, num=i))
                    except:
                        self.sig.emit(self.fprint(
                            "点赞投票时未获取到的错误" + traceback.format_exc(), dlevel=2, num=i))
                    finally:
                        self.pro = self.pro + self.prog
                        self.prosig.emit(int(self.pro))
                        self.wait()
                if self.vote_reply:
                    for i in range(0, int(self.vote_reply_count)):
                        try:
                            response = votego.reply(self.getURL())
                            self.sig.emit(self.fprint(
                                "添加投票评论" + response, dlevel=1, num=i))
                        except:
                            self.sig.emit(self.fprint(
                                "添加投票评论时未获取到的错误" + traceback.format_exc(), dlevel=2, num=i))
                        finally:
                            self.pro = self.pro + self.prog
                            self.prosig.emit(int(self.pro))
                            self.wait()
            except IndexError:
                self.sig.emit(self.fprint("投票互动数量数量超过投票总数", dlevel=2, num=i))
            except:
                self.sig.emit(self.fprint("获取投票列表时未获取到的错误" + traceback.format_exc(), dlevel=2, num=i))
            finally:
                self.wait()

    def runTopic(self):
        try:
            self.prog = 50 / (int(self.add_topic_count) + int(self.topic_control_count) * (
                self.topic_up / 2 + self.topic_reply / 2 * int(self.topic_reply_count)))
        except:
            self.prog = 0
        for i in range(0, int(self.add_topic_count)):
            try:
                response = ybtopic.topic(
                    self.token,
                    self.puid,
                    self.group_id,
                    self.channel_id
                ).add(
                    self.getURL(),
                    self.getURL()
                )
                self.sig.emit(self.fprint("添加话题" + response, dlevel=1, num=i))
            except:
                self.sig.emit(self.fprint("添加话题时未获取到的错误" + traceback.format_exc(), dlevel=2, num=i))
            finally:
                self.pro = self.pro + self.prog
                self.prosig.emit(int(self.pro))
                self.wait()
        topicget = []
        for i in range(0, int(self.topic_control_count)):
            try:
                topicgo = ybtopic.topic(
                    self.token,
                    self.puid,
                    self.group_id,
                    self.channel_id
                )
                if not topicget:
                    topicget = topicgo.get(size=self.topic_control_count)
                self.article_id = topicget[i]["id"]
                if self.topic_up:
                    try:
                        response = topicgo.up(self.article_id)
                        self.sig.emit(self.fprint(
                            "点赞话题" + response, dlevel=1, num=i))
                    except:
                        self.sig.emit(self.fprint(
                            "点赞话题时未获取到的错误" + traceback.format_exc(), dlevel=2, num=i))
                    finally:
                        self.pro = self.pro + self.prog
                        self.prosig.emit(int(self.pro))
                        self.wait()
                if self.topic_reply:
                    for i in range(0, int(self.topic_reply_count)):
                        try:
                            response = topicgo.reply(
                                self.article_id, self.getURL())
                            self.sig.emit(self.fprint(
                                "添加话题评论" + response, dlevel=1, num=i))
                        except:
                            self.sig.emit(self.fprint(
                                "添加话题评论时未获取到的错误" + traceback.format_exc(), dlevel=2, num=i))
                        finally:
                            self.pro = self.pro + self.prog
                            self.prosig.emit(int(self.pro))
                            self.wait()
            except IndexError:
                self.sig.emit(self.fprint("话题互动数量数量超过话题总数", dlevel=2, num=i))
            except:
                self.sig.emit(self.fprint("获取话题列表时未获取到的错误" + traceback.format_exc(), dlevel=2, num=i))
            finally:
                self.wait()

    sig = QtCore.pyqtSignal(str)
    egpasig = QtCore.pyqtSignal(str)
    prosig = QtCore.pyqtSignal(int)
    stopsig = QtCore.pyqtSignal()

    def run(self):
        if self.login():
            self.stopsig.emit()
        self.pro = 0
        self.runVote()
        self.prosig.emit(50)
        self.pro = 50
        self.runTopic()
        self.prosig.emit(100)
        r.close()


class MainWindow(QtWidgets.QMainWindow, Ui_mainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.clearance = dict()
        self.setupUi(self)
        self.lauchButton.released.connect(self.DisableButton)
        self.loginButton.released.connect(self.showLogin)
        QtCore.QCoreApplication.setOrganizationName("simonsmh")
        QtCore.QCoreApplication.setOrganizationDomain("simonsmh.cc")
        QtCore.QCoreApplication.setApplicationName("ybqt")
        self.settings = QtCore.QSettings(os.getcwd() + "/ybqt.ini", QtCore.QSettings.IniFormat)
        self.settings.setFallbacksEnabled(False)
        if os.path.exists(os.getcwd() + "/ybqt.ini"):
            self.resize(self.settings.value('size', QtCore.QSize(501, 501)))
            self.move(self.settings.value('pos', QtCore.QPoint(0, 0)))
            self.tokenLineedit.setText(self.settings.value("token", type=str))
            self.clearance = self.settings.value("clearance", type=str)
            self.add_vote_countSpinbox.setValue(self.settings.value("add_vote_count", 0, type=int))
            self.vote_control_countSpinbox.setValue(self.settings.value("vote_control_count", 0, type=int))
            self.vote_reply_countSpinbox.setValue(self.settings.value("vote_reply_count", 0, type=int))
            self.add_topic_countSpinbox.setValue(self.settings.value("add_topic_count", 0, type=int))
            self.topic_control_countSpinbox.setValue(self.settings.value("topic_control_count", 0, type=int))
            self.topic_reply_countSpinbox.setValue(self.settings.value("topic_reply_count", 0, type=int))
            if not self.settings.value("vote", 0, type=int):
                self.voteCheckbox.setChecked(False)
            if not self.settings.value("vote_up", 0, type=int):
                self.vote_upCheckbox.setChecked(False)
            if not self.settings.value("vote_reply", 0, type=int):
                self.vote_replyCheckbox.setChecked(False)
            if not self.settings.value("topic_up", 0, type=int):
                self.topic_upCheckbox.setChecked(False)
            if not self.settings.value("topic_reply", 0, type=int):
                self.topic_replyCheckbox.setChecked(False)
            self.urlLineedit.setText(self.settings.value("url", type=str))
            self.doubleSpinBox.setValue(self.settings.value("double", 0.0000, type=float))
            self.NotePad.setPlainText(self.settings.value("note", type=str))
        else:
            self.QsettingHook()

    def DisableButton(self):
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText("---运行开始---")
        self.lauchButton.setText("停止")
        self.lauchButton.setDisabled(True)
        self.loginButton.setDisabled(True)
        self.tokenLineedit.setDisabled(True)
        self.add_vote_countSpinbox.setDisabled(True)
        self.vote_control_countSpinbox.setDisabled(True)
        self.vote_reply_countSpinbox.setDisabled(True)
        self.add_topic_countSpinbox.setDisabled(True)
        self.topic_control_countSpinbox.setDisabled(True)
        self.topic_reply_countSpinbox.setDisabled(True)
        self.voteCheckbox.setDisabled(True)
        self.vote_upCheckbox.setDisabled(True)
        self.vote_replyCheckbox.setDisabled(True)
        self.topic_upCheckbox.setDisabled(True)
        self.topic_replyCheckbox.setDisabled(True)
        self.urlLineedit.setDisabled(True)
        self.doubleSpinBox.setDisabled(True)
        self.progressBar.setValue(0)
        self.QsettingHook()
        self.mythread = MyThread(
            self.settings.value("token", type=str),
            self.settings.value("clearance", type=str),
            self.settings.value("captcha", type=str),
            self.settings.value("add_vote_count", 0, type=int),
            self.settings.value("vote_control_count", 0, type=int),
            self.settings.value("vote_reply_count", 0, type=int),
            self.settings.value("add_topic_count", 0, type=int),
            self.settings.value("topic_control_count", 0, type=int),
            self.settings.value("topic_reply_count", 0, type=int),
            self.settings.value("vote", 0, type=int),
            self.settings.value("vote_up", 0, type=int),
            self.settings.value("vote_reply", 0, type=int),
            self.settings.value("topic_up", 0, type=int),
            self.settings.value("topic_reply", 0, type=int),
            self.settings.value("url", type=str),
            self.settings.value("double", 0.0000, type=float)
        )
        self.mythread.sig.connect(self.PrintText)
        self.mythread.prosig.connect(self.Progress)
        self.mythread.egpasig.connect(self.EgpaShowup)
        self.mythread.stopsig.connect(self.StopThread)
        self.mythread.finished.connect(self.EnableButton)
        self.mythread.start()
        self.lauchButton.released.disconnect()
        self.lauchButton.released.connect(self.StopThread)
        self.lauchButton.setEnabled(True)

    def EnableButton(self):
        self.plainTextEdit.appendPlainText("---运行终止---")
        self.lauchButton.setText("启动")
        self.lauchButton.setDisabled(True)
        self.loginButton.setEnabled(True)
        self.tokenLineedit.setEnabled(True)
        self.add_vote_countSpinbox.setEnabled(True)
        self.vote_control_countSpinbox.setEnabled(True)
        self.vote_reply_countSpinbox.setEnabled(True)
        self.add_topic_countSpinbox.setEnabled(True)
        self.topic_control_countSpinbox.setEnabled(True)
        self.topic_reply_countSpinbox.setEnabled(True)
        self.voteCheckbox.setEnabled(True)
        self.vote_upCheckbox.setEnabled(True)
        self.vote_replyCheckbox.setEnabled(True)
        self.topic_upCheckbox.setEnabled(True)
        self.topic_replyCheckbox.setEnabled(True)
        self.urlLineedit.setEnabled(True)
        self.doubleSpinBox.setEnabled(True)
        self.lauchButton.released.disconnect()
        self.lauchButton.released.connect(self.DisableButton)
        self.lauchButton.setEnabled(True)

    def QsettingHook(self):
        self.settings.setValue("WARNNING", "DO NOT EDIT THIS FILE.")
        self.settings.setValue("pos", self.pos())
        self.settings.setValue("size", self.size())
        self.settings.setValue("token", self.tokenLineedit.text())
        self.settings.setValue("clearance", self.clearance)
        self.settings.setValue("add_vote_count", self.add_vote_countSpinbox.text())
        self.settings.setValue("vote_control_count", self.vote_control_countSpinbox.text())
        self.settings.setValue("vote_reply_count", self.vote_reply_countSpinbox.text())
        self.settings.setValue("add_topic_count", self.add_topic_countSpinbox.text())
        self.settings.setValue("topic_control_count", self.topic_control_countSpinbox.text())
        self.settings.setValue("topic_reply_count", self.topic_reply_countSpinbox.text())
        self.settings.setValue("vote", self.voteCheckbox.checkState())
        self.settings.setValue("vote_up", self.vote_upCheckbox.checkState())
        self.settings.setValue("vote_reply", self.vote_replyCheckbox.checkState())
        self.settings.setValue("topic_up", self.topic_upCheckbox.checkState())
        self.settings.setValue("topic_reply", self.topic_replyCheckbox.checkState())
        self.settings.setValue("url", self.urlLineedit.text())
        self.settings.setValue("double", self.doubleSpinBox.text())
        self.settings.setValue("note", self.NotePad.toPlainText())
        self.settings.sync()

    def StopThread(self):
        if self.mythread.isRunning():
            self.mythread.terminate()

    def EgpaShowup(self, string):
        self.setWindowTitle("易班"+string)

    def Progress(self, integer):
        self.progressBar.setValue(integer)

    def PrintText(self, string):
        self.plainTextEdit.appendPlainText(string)

    def closeEvent(self, ev):
        self.QsettingHook()
        loginw.close()
        loginw.deleteLater()
        ev.accept()

    def showLogin(self):
        loginw.show()

class LoginWindow(QtWidgets.QMainWindow, Ui_LoginWindow):

    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        profile = QtWebEngineWidgets.QWebEngineProfile(self.webEngineView)
        webpage = QtWebEngineWidgets.QWebEnginePage(profile, self.webEngineView)
        self.webEngineView.setPage(webpage)
        self.cookie_store = profile.cookieStore()
        self.cookie_store.cookieAdded.connect(self.onCookieAdded)
        self.cookies = dict()
        self.resetWebview()
        self.webEngineView.load(QtCore.QUrl("https://www.yiban.cn/login"))

    def resetWebview(self):
        self.cookie_store.deleteAllCookies()
        self.cookies.clear()

    def onCookieAdded(self, cookie):
        data = {bytearray(QtNetwork.QNetworkCookie(cookie).name()).decode(): bytearray(QtNetwork.QNetworkCookie(cookie).value()).decode()}
        self.cookies.update(data)
        if 'yiban_user_token' in self.cookies:
            mainw.tokenLineedit.setText(self.cookies['yiban_user_token'])
            mainw.clearance = self.cookies['_ydclearance']
            self.resetWebview()
            self.close()

    def closeEvent(self, ev):
        self.resetWebview()
        ev.accept()

if __name__ == "__main__":

    r = requests.Session()
    app = QtWidgets.QApplication(sys.argv)
    mainw = MainWindow()
    loginw = LoginWindow()
    mainw.show()
    sys.exit(app.exec_())
