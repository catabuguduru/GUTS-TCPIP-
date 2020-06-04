if __name__ == '__main__':
    TEST_LOADER = unittest.TestLoader()
    TEST_SUITE = unittest.TestSuite()
    TEST_SUITE.addTests(
        TEST_LOADER.loadTestsFromTestCase(
            TestConnection
        )
    )
    TEST_SUITE.addTests(
        TEST_LOADER.loadTestsFromTestCase(
            TestLogin
        )
    )
    TEST_SUITE.addTests(
        TEST_LOADER.loadTestsFromTestCase(
            TestChangeDirectory
        )
    )
    TEST_SUITE.addTests(
        TEST_LOADER.loadTestsFromTestCase(
            TestReadFile
        )
    )
    TEST_SUITE.addTests(
        TEST_LOADER.loadTestsFromTestCase(
            TestWriteFile
        )
    )
    TEST_SUITE.addTests(
        TEST_LOADER.loadTestsFromTestCase(
            TestRegisterUser
        )
    )
    TEST_SUITE.addTests(
        TEST_LOADER.loadTestsFromTestCase(
            TestDeleteUser
        )
    )
    FLAG = unittest.TextTestRunner(verbosity=2).run(TEST_SUITE)
    if FLAG.skipped:
        print("Error in testing TestConnection")
        sys.exit()
