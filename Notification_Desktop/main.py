""" 
import asyncio
from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier()


async def main():
    n = await notifier.send(title="Testing notofication",message="My python notification")
    await asyncio.sleep(5)
    await notifier.clear(n)
    await notifier.clear_all()
    
asyncio.run(main())

"""
import winsdk.windows.ui.notifications as notifications
import winsdk.windows.data.xml.dom as dom
import sys

notiManager = notifications.ToastNotificationManager
notifier = notiManager.create_toast_notifier(sys.executable)

tString = """
<toast>
    <visual>
        <binding template='ToastGeneric'>
            <text>Sample toast</text>
            <text>Sample content</text>
        </binding>
    </visual>
</toast>

"""
xDoc = dom.XmlDocument()
xDoc.load_xml(tString)

notifier.show(notifications.ToastNotification(xDoc))