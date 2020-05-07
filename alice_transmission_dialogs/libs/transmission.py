# -*- coding: utf-8 -*-
import transmissionrpc


class Transmission(object):
    def __init__(self, address='localhost', port=9091, user='', password=''):
        self.address = address
        self.port = port
        self.user = user
        self.password = password
        self.tc = self.__get_client()

    def __get_client(self):
        return transmissionrpc.Client(self.address, self.port, self.user, self.password)

    def __get_torrents(self):
        return self.tc.get_torrents()

    def get_active_torrent(self):
        torrents = []
        torrent_list = self.__get_torrents()
        for torrent in torrent_list:
            if torrent.status == 'downloading':
                torrents.append(torrent)
        if len(torrents) > 0:
            try:
                for torrent in torrents:
                    if not torrent.doneDate:
                        try:
                            eta = str(torrent.eta)
                        except ValueError:
                            eta = 'Пока неизвестно'
                        torrent_info = u'{}, Процент загрузки: {}%, Осталось до окончания: {}'.format(torrent.name,
                                                                                                      round(torrent.progress, 2),
                                                                                                      eta
                                                                                                      )
            except Exception as exc:
                raise exc
        else:
            torrent_info = 'Сейчас нет активных закачек.'
        return torrent_info
