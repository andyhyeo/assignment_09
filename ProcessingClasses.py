#------------------------------------------#
# Title: Processing Classes
# Desc: A Module for processing Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# AYEO, 2020-Mar-19, added DataProcessor.select_cd method, NOT tested 
# AYEO, 2020-Mar-19, added DataProcessor.add_track, NOT tested 

#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to ran by itself')

import DataClasses as DC

class DataProcessor:
    """Processing the data in the application"""
    @staticmethod
    def add_CD(CDInfo, table):
        """function to add CD info in CDinfo to the inventory table.


        Args:
            CDInfo (tuple): Holds information (ID, CD Title, CD Artist) to be added to inventory.
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """

        cdId, title, artist = CDInfo
        try:
            cdId = int(cdId)
        except:
            raise Exception('ID must be an Integer!')
        row = DC.CD(cdId, title, artist)
        table.append(row)

    @staticmethod
    def select_cd(table: list, cd_idx: int) -> DC.CD:
        """selects a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:
            row (DC.CD): CD object that matches cd_idx

        """
        # TODO add code as required
        try:
            cd_idx = int(cd_idx)
        except ValueError as e:
            print('ID is not an Integer!') 
            print(e.__doc__)
        for row in table:
            if row.cd_id == cd_idx:
                return row
        raise Exception('This CD / Album index does not exist')


    @staticmethod
    def add_track(track_info: tuple, cd: DC.CD) -> None:
        """adds a Track object with attributes in track_info to cd


        Args:
            track_info (tuple): Tuple containing track info (position, title, Length).
            cd (DC.CD): cd object the tarck gets added to.

        Raises:
            Exception: DESCraised in case position is not an integer.

        Returns:
            None: DESCRIPTION.

        """

        # TODO add code as required
        
        trkPos, trkTitle, trkLength = track_info
        try:
            trkPos = int(trkPos)
        except: 
            raise Exception('Postion must be an Integer')
        track = DC.Track(trkPos, trkTitle, trkLength)
        cd.add_track(track)

    @staticmethod
    def delete_cd(table: list, cd_idx: int) -> DC.CD:
        """delete a CD object out of table that has the ID cd_idx

        Args:
            table (list): Inventory list of CD objects.
            cd_idx (int): id of CD object to return

        Raises:
            Exception: If id is not in list.

        Returns:

        """
        intRowNr = -1  
        blnCDRemoved = False  
        for row in table:  
            intRowNr += 1  
            if row.cd_id == int(cd_idx):  
                del table[intRowNr]  
                blnCDRemoved = True  
                break  
            if blnCDRemoved:  
                print('The CD was removed')  
            else:  
                print('Could not find this CD!')      
        return table 
