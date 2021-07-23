"""
based on https://strftime.org/

>>> from mediascope.bdp_python_utils.common import datetime_functions, DTFmt
>>> datetime_functions.now_str()
'15072021-133324'
>>> datetime_functions.now_str(datetime_functions.DTFmt.DMY.THIN)
'15072021'
>>> datetime_functions.now_str(DTFmt.DMY.SPACED)
'15 07 2021'
>>> datetime_functions.now_str(DTFmt.DMY.SLASHED)
'15/07/2021'
>>> datetime_functions.now_str(DTFmt.YMD.SLASHED_AND_HMS_COLON)
'2021/07/15 13:35:46'
"""

import datetime
import typing as t


def compose_str(fields: t.Tuple, divider: str = '') -> str:
    return divider.join(fields)


class YEAR:
    FULL: str = '%Y'  # Year with century as a decimal number.  // 2013
    ONLY: str = '%y'  # Year without century as a zero-padded decimal number.  // 13


class MONTH:
    ZNUM: str = '%m'  # Month as a zero-padded decimal number.
    NUM: str = '%-m'  # Month as a decimal number. (Platform specific)
    ABBR: str = '%b'  # Month as locale’s abbreviated name.
    FULL: str = '%B'  # Month as locale’s full name.


class DAY:
    DOM: str = '%d'  # Day of the month as a zero-padded decimal number.
    ZDOY: str = '%j'  # Day of the year as a zero-padded decimal number.
    DOY: str = '%-j'  # Day of the year as a decimal number. (Platform specific) 	251


class HOUR:
    Z24: str = '%H'  # Hour (24-hour clock) as a zero-padded decimal number.
    NUM24: str = '%-H'  # Hour (24-hour clock) as a decimal number. (Platform specific)
    Z12: str = '%I'  # Hour (12-hour clock) as a zero-padded decimal number.
    NUM12: str = '%-I'  # Hour (12-hour clock) as a decimal number. (Platform specific)
    AMPM: str = '%p'  # Locale’s equivalent of either AM or PM.


class MINUTE:
    ZNUM: str = '%M'  # Minute as a zero-padded decimal number. 	06
    NUM: str = '%-M'  # Minute as a decimal number. (Platform specific) 	6


class SECOND:
    ZNUM: str = '%S'  # Second as a zero-padded decimal number. 	05
    NUM: str = '%-S'  # Second as a decimal number. (Platform specific) 	5
    MSEC: str = '%f'  # Microsecond as a decimal number, zero-padded on the left. 	000000


class HMS:
    _HMS: tuple = (HOUR.Z24, MINUTE.ZNUM, SECOND.ZNUM)

    THIN: str = compose_str(_HMS)
    COLON: str = compose_str(_HMS, divider=':')
    SPACED: str = compose_str(_HMS, divider=' ')
    UNDERSCORED: str = compose_str(_HMS, divider='_')
    DOTTED: str = compose_str(_HMS, divider='.')
    DASHED: str = compose_str(_HMS, divider='-')


class HM:
    _HM: tuple = (HOUR.Z24, MINUTE.ZNUM)

    THIN: str = compose_str(_HM)
    COLON: str = compose_str(_HM, divider=':')
    SPACED: str = compose_str(_HM, divider=' ')
    UNDERSCORED: str = compose_str(_HM, divider='_')
    DOTTED: str = compose_str(_HM, divider='.')
    DASHED: str = compose_str(_HM, divider='-')


class DMY:
    _DMY: tuple = (DAY.DOM, MONTH.ZNUM, YEAR.FULL)

    THIN: str = compose_str(_DMY)
    SPACED: str = compose_str(_DMY, divider=' ')
    UNDERSCORED: str = compose_str(_DMY, divider='_')
    DOTTED: str = compose_str(_DMY, divider='.')
    DASHED: str = compose_str(_DMY, divider='-')
    SLASHED: str = compose_str(_DMY, divider='/')
    BACKSLASHED: str = compose_str(_DMY, divider='\\')

    THIN_DASH_HM_THIN: str = f'{THIN}-{HM.THIN}'
    THIN_DASH_HMS_THIN: str = f'{THIN}-{HMS.THIN}'
    THIN_UNDERSCORE_HM_THIN: str = f'{THIN}_{HM.THIN}'
    THIN_UNDERSCORE_HMS_THIN: str = f'{THIN}_{HMS.THIN}'
    DASHED_UNDERSCORE_HMS_DASHED: str = f'{DASHED}_{HMS.DASHED}'  # '%d-%m-%Y_%H-%M-%S'
    SLASHED_SPACE_HMS_COLON: str = f'{SLASHED} {HMS.COLON}'  # '%d/%m/%Y %H:%M:%S'


class YMD:
    _YMD: tuple = (YEAR.FULL, MONTH.ZNUM, DAY.DOM)

    THIN: str = compose_str(_YMD)
    SPACED: str = compose_str(_YMD, divider=' ')
    UNDERSCORED: str = compose_str(_YMD, divider='_')
    DOTTED: str = compose_str(_YMD, divider='.')
    DASHED: str = compose_str(_YMD, divider='-')
    SLASHED: str = compose_str(_YMD, divider='/')
    BACKSLASHED: str = compose_str(_YMD, divider='\\')

    THIN_DASH_HM_THIN: str = f'{THIN}-{HM.THIN}'
    THIN_DASH_HMS_THIN: str = f'{THIN}-{HMS.THIN}'
    THIN_UNDERSCORE_HM_THIN: str = f'{THIN}_{HM.THIN}'
    THIN_UNDERSCORE_HMS_THIN: str = f'{THIN}_{HMS.THIN}'
    DASHED_UNDERSCORE_HMS_DASHED: str = f'{DASHED}_{HMS.DASHED}'  # '%Y-%m-%d_%H-%M-%S'
    SLASHED_AND_HMS_COLON: str = f'{SLASHED} {HMS.COLON}'  # '2021/07/15 13:35:46'


class WEEKDAY:
    ABBR: str = '%a'  # Weekday as locale’s abbreviated name. 	Sun
    FULL: str = '%A'  # Weekday as locale’s full name. 	Sunday
    NUM: str = '%w'  # Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.


class WEEK:
    # Week number of the year (Sunday as the first day of the week) as a zero padded decimal number.
    # All days in a new year preceding the first Sunday are considered to be in week 0. 	36
    ZOFYEAR: str = '%U'
    # Week number of the year (Monday as the first day of the week) as a decimal number.
    # All days in a new year preceding the first Monday are considered to be in week 0. 	35
    OFYEAR: str = '%W'


class DTFmt:
    SECOND = SECOND
    MINUTE = MINUTE
    HOUR = HOUR

    DAY = DAY
    WEEKDAY = WEEKDAY
    WEEK = WEEK
    MONTH = MONTH
    YEAR = YEAR

    HMS = HMS
    HM = HM
    DMY = DMY
    YMD = YMD

    TZ: str = '%Z'  # Time zone name (empty string if the object is naive).
    LOCALE_DTTM: str = '%c'  # Locale’s appropriate date and time representation.   Sun Sep 8 07:06:05 2013
    LOCALE_DT: str = '%x'  # Locale’s appropriate date representation.   09/08/13
    LOCALE_TM: str = '%X'  # Locale’s appropriate time representation.   07:06:05
    PERCENTAGE: str = '%%'  # A literal '%' character.


def today() -> datetime.date:
    return datetime.date.today()


def now() -> datetime.datetime:
    return datetime.datetime.now()


def f(func: t.Callable, fmt: str) -> str:
    return func().strftime(fmt)


def now_str(fmt: str = DTFmt.LOCALE_DTTM) -> str:
    return f(now, fmt)
