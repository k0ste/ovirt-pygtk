#!/usr/bin/python2

# GPL
# 2015, Konstantin Shalygin (k0ste[at]cn.ru)
# version: 0.1

import pygtk
pygtk.require('2.0')
import gtk
import getpass,subprocess,sys,os.path
from optparse import OptionParser

class LDAPEntry:
  def __init__(self):
    parser = OptionParser()
    parser.add_option('-c', '--command', dest='command', help='Command to execute after login')
    parser.add_option('-d', '--domain', dest='domain', default='domain', help='User domain, show in GUI')
    (options, args) = parser.parse_args()
    if not options.command:
      parser.print_help()
      sys.exit(0)

#Define vars
    self.domain = options.domain
    self.user = getpass.getuser()
#Create new window
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_position(gtk.WIN_POS_CENTER)
    window.set_size_request(250, 100)
    window.set_title('oVirt pyGTK')
    window.set_icon_name('ovirt-pygtk')
#Hande close window button (x)
    window.connect('delete-event', gtk.main_quit)
    vbox = gtk.VBox(False, 0)
    window.add(vbox)
    vbox.show()
#Label
    label = gtk.Label(('Password for %s@%s:') % (self.user, self.domain))
    vbox.pack_start(label, True, True, 0)
    label.show()
#TextBox
    entry = gtk.Entry()
#HidePassword
    entry.set_visibility(False)
    entry.set_max_length(50)
#Handle enter pressing
    entry.connect('activate', self.entry_enter_callback, entry, options.command)
    vbox.pack_start(entry, True, True, 0)
    entry.show()
#Button
    button = gtk.Button(stock=gtk.STOCK_CLOSE)
    button.connect('clicked', lambda w: gtk.main_quit())
    vbox.pack_start(button, True, True, 0)
    button.set_flags(gtk.CAN_DEFAULT)
    button.grab_default()
    button.show()

    hbox = gtk.HBox(False, 0)
    vbox.add(hbox)
    hbox.show()
    window.show()

  def entry_enter_callback(self, widget, entry, command):
#Take text from TextBox
    self.password = entry.get_text()
    self.command = command
#Running command with args
    self.proc = [ 'ovirt-shell', '--password', '%s' % (self.password), '-E', '%s' % (self.command) ]
    subprocess.Popen(self.proc, stdout=subprocess.PIPE)
#Delete password from RAM
    del self.password
    gtk.main_quit()

def main():
#Check ovirt-engine-cli installed or not
  try:
    import ovirtcli
  except ImportError:
    print 'oVirt CLI not found, please install it'
    raise SystemExit
#Check user configuration
  main.user = getpass.getuser()
  main.ovirtshellrc = '.ovirtshellrc'
  main.rcpath = ('/home/%s/%s') % (main.user, main.ovirtshellrc)
  if not os.path.isfile(main.rcpath):
    print ('ovirt-engine-cli user configuration (%s) not found') % (main.rcpath)
    raise SystemExit

  gtk.main()
  return 0

if __name__ == "__main__":
  LDAPEntry()
  main()
