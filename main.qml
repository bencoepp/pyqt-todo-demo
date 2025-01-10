import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 2.15
import Demo 1.0

ApplicationWindow {
    id: root
    visible: true
    width: 400
    height: 300
    title: "Simple QML PyQt6"

    TodoHandler{
        id: todoHandler
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
                id: list
                anchors.fill: parent
                model: todoHandler
                verticalLayoutDirection: ListView.TopToBottom
                delegate: Column {
                    id: columnContent
                    spacing: 4

                    Text {
                        text: "Title: " + title
                    }

                    Text {
                        text: "Description: " + description
                        wrapMode: Text.Wrap
                    }

                    Row {
                        spacing: 20
                        Text {
                            text: "Due: " + dueDate
                        }
                        Text {
                            text: "Author: " + author
                        }
                    }

                    Row {
                        spacing: 20
                        Text {
                            text: "Created: " + created
                        }
                        Text {
                            text: "Updated: " + updated
                        }
                    }

                    CheckBox {
                        text: "Done"
                        checked: done
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
                        todoHandler.create(
                            titleInput.text,
                            descriptionInput.text,
                            dueDateInput.text,
                            autherInput.text,
                            createdInput.text,
                            updatedInput.text,
                            doneInput.checked
                        )
                    }
                }
            }
        }
    }
}