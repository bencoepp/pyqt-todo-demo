import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15
import Demo.Todo 1.0

ApplicationWindow {
    id: root
    visible: true
    width: 400
    height: 300
    title: "Simple QML PyQt6"

    Todo {
        id: myTodo
        title: "Buy groceries"
        description: "Get milk, eggs, bread"
        author: "Ben Cöppicus"
        onTitleChanged: {
            console.log("Title changed to:", title)
        }
    }
    
    RowLayout {
        id: layout
        anchors.fill: parent
        spacing: 0
        Rectangle {
            id: listRectangle
            color: 'grey'
            Layout.fillWidth: true
            Layout.minimumWidth: 50
            Layout.preferredWidth: 100
            Layout.fillHeight: true

            ListView {
                width: 180; height: 200

                model: ListModel {
                    ListElement {
                        title: "Bill Smith"
                        description: "555 3264"
                        dueDate: ""
                        auther: "Ben Cöppicus"
                        created: ""
                        updated: ""
                        done: false
                    }
                }
                delegate: MouseArea{
                    Rectangle{
                        RowLayout{
                            CheckBox{
                                Layout.fillWidth: true
                                Layout.minimumWidth: 50
                                Layout.preferredWidth: 50
                                checked: done
                            }
                            ColumnLayout{
                                Layout.fillWidth: true
                                Layout.minimumWidth: 100
                                Layout.preferredWidth: 150

                                Text{
                                    text: title
                                }
                                Text{
                                    text: description
                                }
                                Text{
                                    text: dueDate
                                }
                                Text{
                                    text: auther
                                }
                                Text{
                                    text: created
                                }
                                Text{
                                    text: updated
                                }
                            }
                        }
                    }
                }
            }
        }

        Rectangle {
            id: inputRectangle
            Layout.fillWidth: true
            Layout.fillHeight: true
            Layout.minimumWidth: 100
            Layout.preferredWidth: 100
            
            ColumnLayout {
                id: inputColumn
                anchors.fill: parent
                spacing: 4
        
                TextField {
                    id: titleInput
                    placeholderText: qsTr("Enter title")
                    Layout.fillWidth: true
                }
                TextField {
                    id: descriptionInput
                    placeholderText: qsTr("Enter description")
                    Layout.fillWidth: true
                }
                RowLayout{
                    CheckBox {
                        id: doneInput
                        checked: false
                        text: qsTr("Done")
                    }
                    TextField {
                        id: dueDateInput
                        placeholderText: qsTr("Enter due date")
                        Layout.fillWidth: true
                    }
                }
                TextField {
                    id: autherInput
                    placeholderText: qsTr("Enter auther")
                    Layout.fillWidth: true
                }
                TextField {
                    id: createdInput
                    Layout.fillWidth: true
                }
                TextField {
                    id: updatedInput
                    Layout.fillWidth: true
                }

                Button{
                    id: saveButton
                    text: "Save"
                    Layout.fillWidth: true
                     onClicked: {
                        
                        myTodo.create()
                    }
                }
            }
        }
    }
}