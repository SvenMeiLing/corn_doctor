# -*- coding: utf-8 -*-
# FileName: store.py
# Time : 2024/6/28 17:09
# Author: zzy

from sqlalchemy import String, Numeric, Integer, ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import BaseOrmTable, TimestampColumns


class ProductOrm(BaseOrmTable, TimestampColumns):
    __tablename__ = 'product'
    __table_args__ = {'comment': '商品表'}

    name: Mapped[str] = mapped_column(String(32), nullable=False, comment='商品名称', index=True)
    price: Mapped[float] = mapped_column(Numeric, nullable=False, comment='商品单价')
    stock_quantity: Mapped[int] = mapped_column(Integer, nullable=False, comment="库存数量")
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('category.id'), nullable=False, comment='类别ID')
    brand: Mapped[str] = mapped_column(String(64), nullable=True, comment='品牌')
    status: Mapped[str] = mapped_column(String(16), nullable=False, default='available', comment='状态')
    image_url: Mapped[str] = mapped_column(
        String(2048), nullable=True,
        comment='图片URL,格式为:xxx.jpg,dfg.png,apple.jpg'
    )
    shipping_method: Mapped[str] = mapped_column(
        String(12), nullable=True, default='包邮', comment='发货方式'
    )
    category: Mapped['CategoryOrm'] = relationship('CategoryOrm', back_populates='products')
    store: Mapped['StoreOrm'] = relationship('StoreOrm', back_populates='products')


class CategoryOrm(BaseOrmTable, TimestampColumns):
    __tablename__ = 'category'
    name: Mapped[str] = mapped_column(String(32), nullable=False, unique=True, comment='商品分类名称')

    products: Mapped[list['ProductOrm']] = relationship('ProductOrm', back_populates='category')


class StoreOrm(BaseOrmTable, TimestampColumns):
    """
    一个店铺对应多个分类, 每个分类对应多个商品
    """
    __tablename__ = 'store'
    name: Mapped[str] = mapped_column(String(32), nullable=False, comment='店铺名称')
    logo_img: Mapped[str] = mapped_column(String(32), comment='logo图片地址')

    products: Mapped[list['ProductOrm']] = relationship('ProductOrm', back_populates='store',
                                                        cascade='all, delete-orphan')
