# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow - untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(501, 501)
        mainWindow.setMinimumSize(QtCore.QSize(451, 301))
        mainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 2, 0, 1, 2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.voteformLayout = QtWidgets.QFormLayout()
        self.voteformLayout.setObjectName("voteformLayout")
        self.add_vote_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.add_vote_countLabel.setObjectName("add_vote_countLabel")
        self.voteformLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.add_vote_countLabel)
        self.add_vote_countSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.add_vote_countSpinbox.setProperty("value", 1)
        self.add_vote_countSpinbox.setObjectName("add_vote_countSpinbox")
        self.voteformLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.add_vote_countSpinbox)
        self.vote_control_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.vote_control_countLabel.setObjectName("vote_control_countLabel")
        self.voteformLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.vote_control_countLabel)
        self.vote_control_countSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.vote_control_countSpinbox.setProperty("value", 2)
        self.vote_control_countSpinbox.setObjectName("vote_control_countSpinbox")
        self.voteformLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.vote_control_countSpinbox)
        self.vote_reply_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.vote_reply_countLabel.setObjectName("vote_reply_countLabel")
        self.voteformLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.vote_reply_countLabel)
        self.vote_reply_countSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.vote_reply_countSpinbox.setProperty("value", 1)
        self.vote_reply_countSpinbox.setObjectName("vote_reply_countSpinbox")
        self.voteformLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.vote_reply_countSpinbox)
        self.gridLayout_2.addLayout(self.voteformLayout, 0, 0, 1, 1)
        self.choiceverticalLayout = QtWidgets.QVBoxLayout()
        self.choiceverticalLayout.setObjectName("choiceverticalLayout")
        self.voteCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.voteCheckbox.setIconSize(QtCore.QSize(10, 10))
        self.voteCheckbox.setChecked(True)
        self.voteCheckbox.setObjectName("voteCheckbox")
        self.choiceverticalLayout.addWidget(self.voteCheckbox, 0, QtCore.Qt.AlignHCenter)
        self.vote_upCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.vote_upCheckbox.setTabletTracking(False)
        self.vote_upCheckbox.setChecked(True)
        self.vote_upCheckbox.setObjectName("vote_upCheckbox")
        self.choiceverticalLayout.addWidget(self.vote_upCheckbox, 0, QtCore.Qt.AlignHCenter)
        self.vote_replyCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vote_replyCheckbox.sizePolicy().hasHeightForWidth())
        self.vote_replyCheckbox.setSizePolicy(sizePolicy)
        self.vote_replyCheckbox.setChecked(True)
        self.vote_replyCheckbox.setObjectName("vote_replyCheckbox")
        self.choiceverticalLayout.addWidget(self.vote_replyCheckbox, 0, QtCore.Qt.AlignHCenter)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.choiceverticalLayout.addWidget(self.line)
        self.topic_upCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.topic_upCheckbox.setChecked(True)
        self.topic_upCheckbox.setObjectName("topic_upCheckbox")
        self.choiceverticalLayout.addWidget(self.topic_upCheckbox, 0, QtCore.Qt.AlignHCenter)
        self.topic_replyCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.topic_replyCheckbox.setChecked(True)
        self.topic_replyCheckbox.setObjectName("topic_replyCheckbox")
        self.choiceverticalLayout.addWidget(self.topic_replyCheckbox, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addLayout(self.choiceverticalLayout, 0, 2, 1, 1)
        self.topicformLayout = QtWidgets.QFormLayout()
        self.topicformLayout.setObjectName("topicformLayout")
        self.add_topic_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.add_topic_countLabel.setObjectName("add_topic_countLabel")
        self.topicformLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.add_topic_countLabel)
        self.add_topic_countSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.add_topic_countSpinbox.setProperty("value", 1)
        self.add_topic_countSpinbox.setObjectName("add_topic_countSpinbox")
        self.topicformLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.add_topic_countSpinbox)
        self.topic_control_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.topic_control_countLabel.setObjectName("topic_control_countLabel")
        self.topicformLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.topic_control_countLabel)
        self.topic_control_countSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.topic_control_countSpinbox.setProperty("value", 2)
        self.topic_control_countSpinbox.setObjectName("topic_control_countSpinbox")
        self.topicformLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.topic_control_countSpinbox)
        self.topic_reply_countSpinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.topic_reply_countSpinbox.setProperty("value", 1)
        self.topic_reply_countSpinbox.setObjectName("topic_reply_countSpinbox")
        self.topicformLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.topic_reply_countSpinbox)
        self.topic_reply_countLabel = QtWidgets.QLabel(self.centralwidget)
        self.topic_reply_countLabel.setObjectName("topic_reply_countLabel")
        self.topicformLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.topic_reply_countLabel)
        self.gridLayout_2.addLayout(self.topicformLayout, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 2)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.usernameLabel = QtWidgets.QLabel(self.centralwidget)
        self.usernameLabel.setWhatsThis("")
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameLineedit.setText("")
        self.usernameLineedit.setObjectName("usernameLineedit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.usernameLineedit)
        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setWhatsThis("")
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordLineedit.setText("")
        self.passwordLineedit.setObjectName("passwordLineedit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.passwordLineedit)
        self.catLabel = QtWidgets.QLabel(self.centralwidget)
        self.catLabel.setWhatsThis("")
        self.catLabel.setObjectName("catLabel")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.catLabel)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.waitLabel = QtWidgets.QLabel(self.centralwidget)
        self.waitLabel.setObjectName("waitLabel")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.waitLabel)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setMinimum(1.0)
        self.doubleSpinBox.setSingleStep(0.2)
        self.doubleSpinBox.setProperty("value", 3.6)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.lauchButton = QtWidgets.QPushButton(self.centralwidget)
        self.lauchButton.setObjectName("lauchButton")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.lauchButton)
        self.gridLayout_3.addLayout(self.formLayout_4, 0, 0, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.comboBox.setCurrentIndex(7)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "易班 EGPA"))
        self.plainTextEdit.setToolTip(_translate("mainWindow", "<html><head/><body><p>程序输出日志，如出错请咨询开发者</p></body></html>"))
        self.add_vote_countLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p>发起投票数量，如不需要请改为0关闭自动发起投票</p></body></html>"))
        self.add_vote_countLabel.setText(_translate("mainWindow", "发起投票数量"))
        self.vote_control_countLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p>操作控制投票帖子数量，如不需要请改为0关闭操作控制投票帖子</p></body></html>"))
        self.vote_control_countLabel.setText(_translate("mainWindow", "投票互动数量"))
        self.vote_reply_countLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p>回复投票次数，如不需要请改为0关闭回复投票</p></body></html>"))
        self.vote_reply_countLabel.setText(_translate("mainWindow", "回复投票次数"))
        self.voteCheckbox.setText(_translate("mainWindow", "开启参与投票"))
        self.vote_upCheckbox.setText(_translate("mainWindow", "开启投票点赞"))
        self.vote_replyCheckbox.setText(_translate("mainWindow", "开启回复投票"))
        self.topic_upCheckbox.setText(_translate("mainWindow", "开启话题点赞"))
        self.topic_replyCheckbox.setText(_translate("mainWindow", "开启回复话题"))
        self.add_topic_countLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p>发起话题数量，如不需要请改为0关闭自动发起话题</p></body></html>"))
        self.add_topic_countLabel.setText(_translate("mainWindow", "发起话题数量"))
        self.topic_control_countLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p>操作控制话题帖子数量，如不需要请改为0关闭操作控制话题帖子</p></body></html>"))
        self.topic_control_countLabel.setText(_translate("mainWindow", "话题互动数量"))
        self.topic_reply_countLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p>回复话题次数，如不需要请改为0关闭回复话题</p></body></html>"))
        self.topic_reply_countLabel.setText(_translate("mainWindow", "回复话题次数"))
        self.usernameLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p>用户名</p></body></html>"))
        self.usernameLabel.setText(_translate("mainWindow", "账号/手机号"))
        self.passwordLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p>密码</p></body></html>"))
        self.passwordLabel.setText(_translate("mainWindow", "密码"))
        self.catLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p>可以选择文本内容，使用了 https://hitokoto.cn/ 的服务</p><table border=\"0\"style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\"cellspacing=\"0\"cellpadding=\"0\"><td rowspan=\"9\"/><td colspan=\"4\"><p>提交不同的参数代表不同的类别，具体：</p></td></tr><tr><td><p>a</p></td><td colspan=\"2\"><p>Anime-动画</p></td><td/></tr><tr><td><p>b</p></td><td colspan=\"2\"><p>Comic–漫画</p></td><td/></tr><tr><td><p>c</p></td><td colspan=\"2\"><p>Game–游戏</p></td><td/></tr><tr><td><p>d</p></td><td colspan=\"2\"><p>Novel–小说</p></td><td/></tr><tr><td><p>e</p></td><td colspan=\"2\"><p>Myself–原创</p></td><td/></tr><tr><td><p>f</p></td><td colspan=\"2\"><p>Internet–来自网络</p></td><td/></tr><tr><td><p>g</p></td><td colspan=\"2\"><p>Other–其他</p></td><td/></tr><tr><td><p>其他不存在参数</p></td><td colspan=\"2\"><p>任意类型随机取得</p></td><td/></tr></table></body></html>"))
        self.catLabel.setText(_translate("mainWindow", "使用的文本内容"))
        self.comboBox.setCurrentText(_translate("mainWindow", "All - 随机"))
        self.comboBox.setItemText(0, _translate("mainWindow", "Anime - 动画"))
        self.comboBox.setItemText(1, _translate("mainWindow", "Comic – 漫画"))
        self.comboBox.setItemText(2, _translate("mainWindow", "Game – 游戏"))
        self.comboBox.setItemText(3, _translate("mainWindow", "Novel – 小说"))
        self.comboBox.setItemText(4, _translate("mainWindow", "Myself – 原创"))
        self.comboBox.setItemText(5, _translate("mainWindow", "Internet – 来自网络"))
        self.comboBox.setItemText(6, _translate("mainWindow", "Other – 其他"))
        self.comboBox.setItemText(7, _translate("mainWindow", "All - 随机"))
        self.waitLabel.setToolTip(_translate("mainWindow", "<html><head/><body><p>每个操作之间的间隔，填入浮点数，开始运行后显示实时EGPA</p></body></html>"))
        self.waitLabel.setText(_translate("mainWindow", "等待时间"))
        self.lauchButton.setText(_translate("mainWindow", "启动"))


class MyThread(QtCore.QThread):

    def __init__(self, username, password, add_vote_count, vote_control_count, vote_reply_count, add_topic_count, topic_control_count, topic_reply_count, vote, vote_up, vote_reply, topic_up, topic_reply, cat, waitime):
        super(MyThread, self).__init__()
        self.username = username
        self.password = password
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
        self.cat = cat
        self.waitime = waitime

    def getHitokoto(self):
        cato = {
            0: "a",
            1: "b",
            2: "c",
            3: "d",
            4: "e",
            5: "f",
            6: "g",
            7: "all",
        }
        Get_Hitokoto = r.get("https://sslapi.hitokoto.cn/",
                             params={"c": cato.get(self.cat), "encode": "json"}, timeout=10)
        Hitokoto = Get_Hitokoto.json()["hitokoto"]
        From = Get_Hitokoto.json()["from"]
        return Hitokoto + " --" + From

    def wait(self):
        try:
            self.getEPGA()
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
            self.sig.emit("账号: " + self.username)
            self.sig.emit("密码: " + self.password)
            yiban_user_token = getUserToken(self.username, self.password)
            self.sig.emit("易班 Token: " + yiban_user_token)
            self.token = dict(yiban_user_token=yiban_user_token)
            self.info = getInfo(self.token)
            self.group_id = self.info["group_id"]
            self.puid = self.info["puid"]
            self.channel_id = self.info["channel_id"]
            self.actor_id = self.info["actor_id"]
            self.nick = self.info["nick"]
            self.sig.emit(self.fprint("登陆成功", dlevel=1))
            return 0
        except:
            self.sig.emit(self.fprint("无法连接服务器或密码错误", dlevel=3))
            return 2
        finally:
            self.wait()

    def getEPGA(self):
        try:
            Get_EPGA = r.get(BASEURL + "newgroup/indexPub/group_id/" +
                             self.group_id + "/puid/" + self.puid, cookies=self.token, timeout=10)
            EPGA = re.search(r"EGPA：[0-9\.]*", Get_EPGA.text)
            self.epgasig.emit(EPGA.group())
        except:
            self.epgasig.emit("无法连接服务器")

    def runVote(self):
        try:
            self.prog = 50 / (int(self.add_vote_count) + int(self.vote_control_count)
                          * (self.vote / 2 + self.vote / 2 + self.vote_reply / 2 * int(self.vote_reply_count)))
        except:
            self.prog = 0
        for i in range(0, int(self.add_vote_count)):
            try:
                response = ybvote.vote(
                    self.token,
                    self.puid,
                    self.group_id
                ).add(
                    self.getHitokoto(),
                    self.getHitokoto(),
                    self.getHitokoto(),
                    self.getHitokoto()
                )
                self.sig.emit(self.fprint("添加投票 " + response, dlevel=1, num=i))
            except:
                self.sig.emit(self.fprint("添加投票时未获取到的错误", dlevel=2, num=i))
            finally:
                self.pro = self.pro + self.prog
                self.prosig.emit(self.pro)
                self.wait()

        for i in range(0, int(self.vote_control_count)):
            try:
                self.vote_id = ybvote.vote(
                    self.token,
                    self.puid,
                    self.group_id
                ).get(
                    self.vote_control_count
                )["data"]["list"][i]["id"]
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
                            "参与投票 " + response, dlevel=1, num=i))
                    except:
                        self.sig.emit(self.fprint(
                            "参与投票时未获取到的错误", dlevel=2, num=i))
                    finally:
                        self.pro = self.pro + self.prog
                        self.prosig.emit(self.pro)
                        self.wait()
                if self.vote_up:
                    try:
                        response = votego.up()
                        self.sig.emit(self.fprint(
                            "点赞投票 " + response, dlevel=1, num=i))
                    except:
                        self.sig.emit(self.fprint(
                            "点赞投票时未获取到的错误", dlevel=2, num=i))
                    finally:
                        self.pro = self.pro + self.prog
                        self.prosig.emit(self.pro)
                        self.wait()
                if self.vote_reply:
                    for i in range(0, int(self.vote_reply_count)):
                        try:
                            response = votego.reply(self.getHitokoto())
                            self.sig.emit(self.fprint(
                                "添加投票评论 " + response, dlevel=1, num=i))
                        except:
                            self.sig.emit(self.fprint(
                                "添加投票评论时未获取到的错误", dlevel=2, num=i))
                        finally:
                            self.pro = self.pro + self.prog
                            self.prosig.emit(self.pro)
                            self.wait()
            except:
                self.sig.emit(self.fprint("获取投票列表时未获取到的错误", dlevel=2, num=i))
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
                    self.getHitokoto(),
                    self.getHitokoto()
                )
                self.sig.emit(self.fprint("添加话题 " + response, dlevel=1, num=i))
            except:
                self.sig.emit(self.fprint("添加话题时未获取到的错误", dlevel=2, num=i))
            finally:
                self.pro = self.pro + self.prog
                self.prosig.emit(self.pro)
                self.wait()
        for i in range(0, int(self.topic_control_count)):
            try:
                topicgo = ybtopic.topic(
                    self.token,
                    self.puid,
                    self.group_id,
                    self.channel_id
                )
                self.article_id = topicgo.get(self.topic_control_count)[
                    "data"]["list"][i]["id"]
                if self.topic_up:
                    try:
                        response = topicgo.up(self.article_id)
                        self.sig.emit(self.fprint(
                            "点赞话题 " + response, dlevel=1, num=i))
                    except:
                        self.sig.emit(self.fprint(
                            "点赞话题时未获取到的错误", dlevel=2, num=i))
                    finally:
                        self.pro = self.pro + self.prog
                        self.prosig.emit(self.pro)
                        self.wait()
                if self.topic_reply:
                    for i in range(0, int(self.topic_reply_count)):
                        try:
                            response = topicgo.reply(
                                self.article_id, self.getHitokoto())
                            self.sig.emit(self.fprint(
                                "添加话题评论 " + response, dlevel=1, num=i))
                        except:
                            self.sig.emit(self.fprint(
                                "添加话题评论时未获取到的错误", dlevel=2, num=i))
                        finally:
                            self.pro = self.pro + self.prog
                            self.prosig.emit(self.pro)
                            self.wait()
            except:
                self.sig.emit(self.fprint("获取话题列表时未获取到的错误", dlevel=2, num=i))
            finally:
                self.wait()

    sig = QtCore.pyqtSignal(str)
    epgasig = QtCore.pyqtSignal(str)
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


class MyWindow(QtWidgets.QMainWindow, Ui_mainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.lauchButton.released.connect(self.DisableButton)
        QtCore.QCoreApplication.setOrganizationName("simonsmh")
        QtCore.QCoreApplication.setOrganizationDomain("simonsmh.cc")
        QtCore.QCoreApplication.setApplicationName("ybqt")
        self.settings = QtCore.QSettings(os.getcwd() + "/ybqt.ini", QtCore.QSettings.IniFormat)
        self.settings.setFallbacksEnabled(False)
        if os.path.exists(os.getcwd() + "/ybqt.ini"):
            self.resize(self.settings.value('size', QtCore.QSize(501, 501)))
            self.move(self.settings.value('pos', QtCore.QPoint(0, 0)))
            self.usernameLineedit.setText(self.settings.value("username", type=str))
            self.passwordLineedit.setText(self.settings.value("password", type=str))
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
            self.comboBox.setCurrentIndex(self.settings.value("combo", 0, type=int))
            self.doubleSpinBox.setValue(self.settings.value("double", 0.0000, type=float))
        else:
            self.QsettingHook()

    def DisableButton(self):
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText("---运行开始---")
        self.lauchButton.setText("停止")
        self.lauchButton.setDisabled(True)
        self.usernameLineedit.setDisabled(True)
        self.passwordLineedit.setDisabled(True)
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
        self.comboBox.setDisabled(True)
        self.doubleSpinBox.setDisabled(True)
        self.progressBar.setValue(0)
        self.QsettingHook()
        self.mythread = MyThread(
            self.settings.value("username", type=str),
            self.settings.value("password", type=str),
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
            self.settings.value("combo", 0, type=int),
            self.settings.value("double", 0.0000, type=float)
        )
        self.mythread.sig.connect(self.PrintText)
        self.mythread.prosig.connect(self.Progress)
        self.mythread.epgasig.connect(self.EpgaShowup)
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
        self.usernameLineedit.setEnabled(True)
        self.passwordLineedit.setEnabled(True)
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
        self.comboBox.setEnabled(True)
        self.doubleSpinBox.setEnabled(True)
        self.lauchButton.released.disconnect()
        self.lauchButton.released.connect(self.DisableButton)
        self.lauchButton.setEnabled(True)

    def QsettingHook(self):
        self.settings.setValue("WARNNING", "DO NOT EDIT THIS FILE.")
        self.settings.setValue("pos", self.pos())
        self.settings.setValue("size", self.size())
        self.settings.setValue("username", self.usernameLineedit.text())
        self.settings.setValue("password", self.passwordLineedit.text())
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
        self.settings.setValue("combo", self.comboBox.currentIndex())
        self.settings.setValue("double", self.doubleSpinBox.text())
        self.settings.sync()

    def StopThread(self):
        if self.mythread.isRunning():
            self.mythread.terminate()

    def EpgaShowup(self, string):
        self.waitLabel.setText(string)

    def Progress(self, integer):
        self.progressBar.setValue(integer)

    def PrintText(self, string):
        self.plainTextEdit.appendPlainText(string)

    def closeEvent(self, ev):
        self.QsettingHook()
        ev.accept()

if __name__ == "__main__":
    import os
    import sys
    import re
    import json
    import time
    import getopt
    import random
    import requests
    import ybvote
    import ybtopic
    from yblogin import BASEURL, getUserToken, getInfo
    r = requests.Session()
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWindow()
    widget.show()
    sys.exit(app.exec_())
