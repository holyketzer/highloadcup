# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Area(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, pos_x: int=None, pos_y: int=None, size_x: int=None, size_y: int=None):  # noqa: E501
        """Area - a model defined in Swagger

        :param pos_x: The pos_x of this Area.  # noqa: E501
        :type pos_x: int
        :param pos_y: The pos_y of this Area.  # noqa: E501
        :type pos_y: int
        :param size_x: The size_x of this Area.  # noqa: E501
        :type size_x: int
        :param size_y: The size_y of this Area.  # noqa: E501
        :type size_y: int
        """
        self.swagger_types = {
            'pos_x': int,
            'pos_y': int,
            'size_x': int,
            'size_y': int
        }

        self.attribute_map = {
            'pos_x': 'posX',
            'pos_y': 'posY',
            'size_x': 'sizeX',
            'size_y': 'sizeY'
        }
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._size_x = size_x
        self._size_y = size_y

    @classmethod
    def from_dict(cls, dikt) -> 'Area':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The area of this Area.  # noqa: E501
        :rtype: Area
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pos_x(self) -> int:
        """Gets the pos_x of this Area.


        :return: The pos_x of this Area.
        :rtype: int
        """
        return self._pos_x

    @pos_x.setter
    def pos_x(self, pos_x: int):
        """Sets the pos_x of this Area.


        :param pos_x: The pos_x of this Area.
        :type pos_x: int
        """
        if pos_x is None:
            raise ValueError("Invalid value for `pos_x`, must not be `None`")  # noqa: E501

        self._pos_x = pos_x

    @property
    def pos_y(self) -> int:
        """Gets the pos_y of this Area.


        :return: The pos_y of this Area.
        :rtype: int
        """
        return self._pos_y

    @pos_y.setter
    def pos_y(self, pos_y: int):
        """Sets the pos_y of this Area.


        :param pos_y: The pos_y of this Area.
        :type pos_y: int
        """
        if pos_y is None:
            raise ValueError("Invalid value for `pos_y`, must not be `None`")  # noqa: E501

        self._pos_y = pos_y

    @property
    def size_x(self) -> int:
        """Gets the size_x of this Area.


        :return: The size_x of this Area.
        :rtype: int
        """
        return self._size_x

    @size_x.setter
    def size_x(self, size_x: int):
        """Sets the size_x of this Area.


        :param size_x: The size_x of this Area.
        :type size_x: int
        """

        self._size_x = size_x

    @property
    def size_y(self) -> int:
        """Gets the size_y of this Area.


        :return: The size_y of this Area.
        :rtype: int
        """
        return self._size_y

    @size_y.setter
    def size_y(self, size_y: int):
        """Sets the size_y of this Area.


        :param size_y: The size_y of this Area.
        :type size_y: int
        """

        self._size_y = size_y