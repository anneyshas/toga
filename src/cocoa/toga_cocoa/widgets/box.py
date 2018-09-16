from rubicon.objc import *

from toga_cocoa.libs import NSColor, NSView
from toga_cocoa.resources.colors import native_color

from .base import Widget


class TogaView(NSView):
    @objc_method
    def isFlipped(self) -> bool:
        # Default Cocoa coordinate frame is around the wrong way.
        return True

    @objc_method
    def display(self) -> None:
        self.layer.needsDisplay = True
        self.layer.displayIfNeeded()


class Box(Widget):
    def create(self):
        self.native = TogaView.alloc().init()
        self.native.wantsLayer = True

        # Add the layout constraints
        self.add_constraints()

    def set_background_color(self, value):
        if value is None:
            self.native.backgroundColor = NSColor.windowBackgroundColor
        else:
            self.native.backgroundColor = native_color(value)
