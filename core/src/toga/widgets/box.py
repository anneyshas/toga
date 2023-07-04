from __future__ import annotations

from .base import Widget


class Box(Widget):
    def __init__(
        self,
        id=None,
        style=None,
        children: list[Widget] | None = None,
    ):
        """Create a new Box container widget.

        Inherits from :class:`toga.Widget`.

        :param id: The ID for the widget.
        :param style: A style object. If no style is provided, a default style
            will be applied to the widget.
        :param children: An optional list of children for to add to the Box.
        """
        super().__init__(id=id, style=style)

        # Children need to be added *before* the impl is created. Otherwise, GTK
        # doesn't apply custom loaded fonts that have been on child widgets.
        self._children = []
        if children:
            self.add(*children)

        # Create a platform specific implementation of a Box
        self._impl = self.factory.Box(interface=self)

    @property
    def enabled(self) -> bool:
        """Is the widget currently enabled? i.e., can the user interact with the widget?

        Box widgets cannot be disabled; this property will always return True; any
        attempt to modify it will be ignored.
        """
        return True

    @enabled.setter
    def enabled(self, value):
        pass

    def focus(self):
        """No-op; Box cannot accept input focus."""
        pass
