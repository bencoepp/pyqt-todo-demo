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

    property int editIndex: -1
    
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

                    Button{
                        Layout.fillWidth: true
                        text: "Edit"
                        onClicked: {
                            console.log(index)
                            editIndex = index
                            titleInput.text = title
                            descriptionInput.text = description
                            dueDateInput.text = dueDate
                            doneInput.checked = done
                            autherInput.text = auther
                            updatedInput.text = updated
                            createdInput.text = created
                    
                        }
                    }

                    Button{
                        Layout.fillWidth: true
                        text: "Delete"
                        onClicked: {
                            todoHandler.delete(index)
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
                        if(editIndex != -1){
                            todoHandler.update(
                                titleInput.text,
                                descriptionInput.text,
                                dueDateInput.text,
                                autherInput.text,
                                createdInput.text,
                                updatedInput.text,
                                doneInput.checked,
                                editIndex
                            )
                            editIndex = -1
                        }else{
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

                        titleInput.clear()
                        descriptionInput.clear()
                        dueDateInput.clear()
                        autherInput.clear()
                        createdInput.clear()
                        updatedInput.clear()
                        doneInput.checked = false
                    }
                }

                Button{
                    id: cancelButton
                    text: "Cancel"
                    Layout.fillWidth: true
                     onClicked: {
                        editIndex = -1

                        titleInput.clear()
                        descriptionInput.clear()
                        dueDateInput.clear()
                        autherInput.clear()
                        createdInput.clear()
                        updatedInput.clear()
                        doneInput.checked = false
                    }
                }
            }
        }
    }
}