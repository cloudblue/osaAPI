import base64
import random
import string
import sys
import time

if sys.version_info[0] < 3:
    import xmlrpclib as client
else:
    from xmlrpc import client


def rand_id(max_size=10, chars=string.ascii_uppercase + string.digits):
    size = random.randint(min(max_size, 5), max_size)
    return ''.join(random.choice(chars) for x in range(size))


class PBA(object):
    def __init__(self, host, user=None, password=None, ssl=False, verbose=False, port=5224):
        protocol = 'https' if ssl else 'http'
        if user:
            self.__server__ = client.ServerProxy(
                "%s://%s:%s@%s:%s/RPC2" % (protocol, user, password, host, str(port)))
        else:
            self.__server__ = client.ServerProxy("%s://%s:%s/RPC2" % (protocol, host, str(port)))
        self.__server__._ServerProxy__verbose = verbose
        self.host = host

    def Execute(self, method, params=None, server='BM'):
        if not params:
            params = []
        v = {
            'Params': params,
            'Server': server,
            'Method': method,
        }
        try:
            response = {
                'status': 0,
                'result': self.__server__.Execute(v)['Result'].pop(),
            }
            return response
        except client.Fault as err:
            response = {
                'error_message': base64.b64decode(err.faultString).strip(),
                'status': -1,
                'method': method,
                'params': params,
                'server': server,
                'host': self.host,
                'result': None,
            }
            return response


class OSA(object):
    def __init__(self, host, user=None, password=None, ssl=False, verbose=False, port=8440):
        protocol = 'https' if ssl else 'http'
        if user:
            self.__server__ = client.ServerProxy(
                "%s://%s:%s@%s:%s/RPC2" % (protocol, user, password, host, str(port)))
        else:
            self.__server__ = client.ServerProxy("%s://%s:%s/RPC2" % (protocol, host, str(port)))
        self.__server__._ServerProxy__verbose = verbose

    # PPA only
    @property
    class msp_license_manager(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def uploadMainLicense(self, **kwargs):
            return self.__server__.pem.msp_license_manager.uploadMainLicense(kwargs)

    @property
    def APS(self):
        return self.aps

    @property
    def am(self):
        return self.AM

    @property
    def exchange(self):
        return self.EXCHANGE

    @property
    def sharepoint(self):
        return self.SHAREPOINT

    @property
    def global_relay(self):
        return self.GLOBAL_RELAY

    @property
    def virtuozzo(self):
        return self.VZZP

    @property
    def ocs(self):
        return self.OCS

    @property
    def iis(self):
        return self.IIS

    @property
    def web_cluster(self):
        return self.WEB_CLUSTER

    @property
    def ProFTPD(self):
        return self.PROFTPD

    @property
    def ad(self):
        return self.AD

    @property
    def mscrm(self):
        return self.MSCRM

    @property
    def mssql(self):
        return self.MSSQL

    @property
    def mysql(self):
        return self.MYSQL

    @property
    def cqmail(self):
        return self.CQMAIL

    @property
    def spam_assassin(self):
        return self.SPAM_ASSASSIN

    @property
    def statistics(self):
        return self.STATISTICS

    @property
    def packaging(self):
        return self.PACKAGING

    @property
    def txn(self):
        return self.TXN

    @property
    def tasks(self):
        return self.TASKS

    """
    Management of Accounts and Account's Staff Members
    """

    def addAccount(self, **kwargs):
        return self.__server__.pem.addAccount(kwargs)

    def addAccountMember(self, **kwargs):
        return self.__server__.pem.addAccountMember(kwargs)

    def checkPassword(self, **kwargs):
        return self.__server__.pem.checkPassword(kwargs)

    def disableAccount(self, **kwargs):
        return self.__server__.pem.disableAccount(kwargs)

    def disableAccountMember(self, **kwargs):
        return self.__server__.pem.disableAccountMember(kwargs)

    def enableAccount(self, **kwargs):
        return self.__server__.pem.enableAccount(kwargs)

    def enableAccountMember(self, **kwargs):
        return self.__server__.pem.enableAccountMember(kwargs)

    def getAccountInfo(self, **kwargs):
        return self.__server__.pem.getAccountInfo(kwargs)

    def getAccountMemberByLogin(self, **kwargs):
        return self.__server__.pem.getAccountMemberByLogin(kwargs)

    def getAccountSubscriptions(self, **kwargs):
        return self.__server__.pem.getAccountSubscriptions(kwargs)

    def promoteToReseller(self, **kwargs):
        return self.__server__.pem.promoteToReseller(kwargs)

    def removeAccount(self, **kwargs):
        return self.__server__.pem.removeAccount(kwargs)

    def removeAccountMember(self, **kwargs):
        return self.__server__.pem.removeAccountMember(kwargs)

    def setAccountAuthData(self, **kwargs):
        return self.__server__.pem.setAccountAuthData(kwargs)

    def setAccountInfo(self, **kwargs):
        return self.__server__.pem.setAccountInfo(kwargs)

    def setMemberInfo(self, **kwargs):
        return self.__server__.pem.setMemberInfo(kwargs)

    def setMemberPassword(self, **kwargs):
        return self.__server__.pem.setMemberPassword(kwargs)

    def setSystemProperty(self, **kwargs):
        return self.__server__.pem.setSystemProperty(kwargs)

    def getVendorCustomers(self, **kwargs):
        return self.__server__.pem.getVendorCustomers(kwargs)

    def getAccountRoles(self, **kwargs):
        return self.__server__.pem.getAccountRoles(kwargs)

    def getAccountMemberRoles(self, **kwargs):
        return self.__server__.pem.getAccountMemberRoles(kwargs)

    def getUserFullInfo(self, **kwargs):
        return self.__server__.pem.getUserFullInfo(kwargs)

    def getMemberFullInfo(self, **kwargs):
        return self.__server__.pem.getMemberFullInfo(kwargs)

    def assignRolesToMember(self, **kwargs):
        return self.__server__.pem.assignRolesToMember(kwargs)

    def revokeRolesFromMember(self, **kwargs):
        return self.__server__.pem.revokeRolesFromMember(kwargs)

    """
    Subscriptions Management
    """

    def activateSubscription(self, **kwargs):
        return self.__server__.pem.activateSubscription(kwargs)

    def addSubscription(self, **kwargs):
        return self.__server__.pem.addSubscription(kwargs)

    def disableSubscription(self, **kwargs):
        return self.__server__.pem.disableSubscription(kwargs)

    def enableSubscription(self, **kwargs):
        return self.__server__.pem.enableSubscription(kwargs)

    def getMemberSubscriptionRestrictions(self, **kwargs):
        return self.__server__.pem.getMemberSubscriptionRestrictions(kwargs)

    def getSubscription(self, **kwargs):
        return self.__server__.pem.getSubscription(kwargs)

    def removeSubscription(self, **kwargs):
        return self.__server__.pem.removeSubscription(kwargs)

    def setMemberSubscriptionRestrictions(self, **kwargs):
        return self.__server__.pem.setMemberSubscriptionRestrictions(kwargs)

    def setSubscriptionName(self, **kwargs):
        return self.__server__.pem.setSubscriptionName(kwargs)

    def upgradeSubscription(self, **kwargs):
        return self.__server__.pem.upgradeSubscription(kwargs)

    def getCustomerSubscriptions(self, **kwargs):
        return self.__server__.pem.getCustomerSubscriptions(kwargs)

    """
    Domains Management
    """

    def addDNSHosting(self, **kwargs):
        return self.__server__.pem.addDNSHosting(kwargs)

    def addDomain(self, **kwargs):
        return self.__server__.pem.addDomain(kwargs)

    def addDomainRequest(self, **kwargs):
        return self.__server__.pem.addDomainRequest(kwargs)

    def addDomainToAccount(self, **kwargs):
        return self.__server__.pem.addDomainToAccount(kwargs)

    def addPTRRecord(self, **kwargs):
        return self.__server__.pem.addPTRRecord(kwargs)

    def addSubdomain(self, **kwargs):
        return self.__server__.pem.addSubdomain(kwargs)

    def bindServicesToDomain(self, **kwargs):
        return self.__server__.pem.bindServicesToDomain(kwargs)

    def createDNSRecord(self, **kwargs):
        return self.__server__.pem.createDNSRecord(kwargs)

    def deleteDNSRecord(self, **kwargs):
        return self.__server__.pem.deleteDNSRecord(kwargs)

    def disableDNSRecord(self, **kwargs):
        return self.__server__.pem.disableDNSRecord(kwargs)

    def disableDomain(self, **kwargs):
        return self.__server__.pem.disableDomain(kwargs)

    def enableDNSRecord(self, **kwargs):
        return self.__server__.pem.enableDNSRecord(kwargs)

    def enableDomain(self, **kwargs):
        return self.__server__.pem.enableDomain(kwargs)

    def getDomainByName(self, **kwargs):
        return self.__server__.pem.getDomainByName(kwargs)

    def getDomainList(self, **kwargs):
        return self.__server__.pem.getDomainList(kwargs)

    def getDomainSubscription(self, **kwargs):
        return self.__server__.pem.getDomainSubscription(kwargs)

    def getDNSRecords(self, **kwargs):
        return self.__server__.pem.getDNSRecords(kwargs)

    def getAccountDomains(self, **kwargs):
        return self.__server__.pem.getAccountDomains(kwargs)

    def getNameServers(self, **kwargs):
        return self.__server__.pem.getNameServers(kwargs)

    def getDomainNameServers(self, **kwargs):
        return self.__server__.pem.getDomainNameServers(kwargs)

    def getRequiredNameServers(self, **kwargs):
        return self.__server__.pem.getRequiredNameServers(kwargs)

    def importCertificate(self, **kwargs):
        return self.__server__.pem.importCertificate(kwargs)

    def removeDNSHosting(self, **kwargs):
        return self.__server__.pem.removeDNSHosting(kwargs)

    def removeDomain(self, **kwargs):
        return self.__server__.pem.removeDomain(kwargs)

    def removeDomainRequest(self, **kwargs):
        return self.__server__.pem.removeDomainRequest(kwargs)

    def removePTRRecord(self, **kwargs):
        return self.__server__.pem.removePTRRecord(kwargs)

    def setDomainRegistrarStatus(self, **kwargs):
        return self.__server__.pem.setDomainRegistrarStatus(kwargs)

    def syncNameServers(self, **kwargs):
        return self.__server__.pem.syncNameServers(kwargs)

    def unbindServicesFromDomain(self, **kwargs):
        return self.__server__.pem.unbindServicesFromDomain(kwargs)

    """
    Webspace Management
    """

    def getFTPUser(self, **kwargs):
        return self.__server__.pem.getFTPUser(kwargs)

    def getSubscriptionWebspaces(self, **kwargs):
        return self.__server__.pem.getSubscriptionWebspaces(kwargs)

    def getWebspacesList(self, **kwargs):
        return self.__server__.pem.getWebspacesList(kwargs)

    def setFTPPassword(self, **kwargs):
        return self.__server__.pem.setFTPPassword(kwargs)

    @property
    class APACHE(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def turnWebStatProcessingOn(self, **kwargs):
            return self.__server__.pem.apache.turnWebStatProcessingOn(kwargs)

        def turnWebStatProcessingOff(self, **kwargs):
            return self.__server__.pem.apache.turnWebStatProcessingOff(kwargs)

    @property
    class WEB_CLUSTER(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def changeNFS(self, **kwargs):
            return self.__server__.pem.web_cluster.changeNFS(kwargs)

    @property
    class PROFTPD(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def createCustomFTPUser(self, **kwargs):
            return self.__server__.pem.ProFTPD.createCustomFTPUser(kwargs)

        def deleteCustomFTPUser(self, **kwargs):
            return self.__server__.pem.ProFTPD.deleteCustomFTPUser(kwargs)

        def getCustomFTPUsersList(self, **kwargs):
            return self.__server__.pem.ProFTPD.getCustomFTPUsersList(kwargs)

    @property
    class IIS(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def getSubscriptionSharePointSites(self, **kwargs):
            return self.__server__.pem.iis.getSubscriptionSharePointSites(kwargs)

        def getSubscriptionWebsites(self, **kwargs):
            return self.__server__.pem.iis.getSubscriptionWebsites(kwargs)

        def getWebspaceFeaturesInfo(self, **kwargs):
            return self.__server__.pem.iis.getWebspaceFeaturesInfo(kwargs)

        def getWebspacesInfo(self, **kwargs):
            return self.__server__.pem.iis.getWebspacesInfo(kwargs)

        def setWebspaceFeaturesInfo(self, **kwargs):
            return self.__server__.pem.iis.setWebspaceFeaturesInfo(kwargs)

        def updateLimits(self, **kwargs):
            return self.__server__.pem.iis.updateLimits(kwargs)

        def updatePHPExtensionsList(self, **kwargs):
            return self.__server__.pem.iis.updatePHPExtensionsList(kwargs)

        def addDomainMapping(self, **kwargs):
            return self.__server__.pem.iis.addDomainMapping(kwargs)

        def addSystemMapping(self, **kwargs):
            return self.__server__.pem.iis.addSystemMapping(kwargs)

        def applySystemMappingsToHosts(self, **kwargs):
            return self.__server__.pem.iis.applySystemMappingsToHosts(kwargs)

        def bulkAddDomainMapping(self, **kwargs):
            return self.__server__.pem.iis.bulkAddDomainMapping(kwargs)

        def deleteSystemMapping(self, **kwargs):
            return self.__server__.pem.iis.deleteSystemMapping(kwargs)

        def getDomainEngines(self, **kwargs):
            return self.__server__.pem.iis.getDomainEngines(kwargs)

        def getDomainMapping(self, **kwargs):
            return self.__server__.pem.iis.getDomainMapping(kwargs)

        def getDomainMappings(self, **kwargs):
            return self.__server__.pem.iis.getDomainMappings(kwargs)

        def getSystemEngines(self, **kwargs):
            return self.__server__.pem.iis.getSystemEngines(kwargs)

        def getSystemMapping(self, **kwargs):
            return self.__server__.pem.iis.getSystemMapping(kwargs)

        def getSystemMappings(self, **kwargs):
            return self.__server__.pem.iis.getSystemMappings(kwargs)

        def resetDomainMapping(self, **kwargs):
            return self.__server__.pem.iis.resetDomainMapping(kwargs)

        def setDomainMappingEnabled(self, **kwargs):
            return self.__server__.pem.iis.setDomainMappingEnabled(kwargs)

        def updateDomainMapping(self, **kwargs):
            return self.__server__.pem.iis.updateDomainMapping(kwargs)

        def updateSystemEngine(self, **kwargs):
            return self.__server__.pem.iis.updateSystemEngine(kwargs)

        def updateSystemMapping(self, **kwargs):
            return self.__server__.pem.iis.updateSystemMapping(kwargs)

        def grantAuthorizedWebAccess(self, **kwargs):
            return self.__server__.pem.iis.grantAuthorizedWebAccess(kwargs)

        def revokeAuthorizedWebAccess(self, **kwargs):
            return self.__server__.pem.iis.revokeAuthorizedWebAccess(kwargs)

        def getAuthorizedWebAccessDomainsForUser(self, **kwargs):
            return self.__server__.pem.iis.getAuthorizedWebAccessDomainsForUser(kwargs)

        def getAuthorizedWebAccessUsersForDomain(self, **kwargs):
            return self.__server__.pem.iis.getAuthorizedWebAccessUsersForDomain(kwargs)

        def getFTPAccessStatusForUser(self, **kwargs):
            return self.__server__.pem.iis.getFTPAccessStatusForUser(kwargs)

        def getFTPAccessStatusesForDomain(self, **kwargs):
            return self.__server__.pem.iis.getFTPAccessStatusesForDomain(kwargs)

        def grantFTPAccessToWebsite(self, **kwargs):
            return self.__server__.pem.iis.grantFTPAccessToWebsite(kwargs)

        def revokeFTPAccessFromWebsite(self, **kwargs):
            return self.__server__.pem.iis.revokeFTPAccessFromWebsite(kwargs)

    @property
    class OCS(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def getPhoneNumberList(self, **kwargs):
            return self.__server__.pem.ocs.getPhoneNumberList(kwargs)

    """
    Service User Management
    """

    @property
    class AD(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        @property
        def binding(self):
            return self.BINDING

        @property
        class BINDING(object):
            def __init__(self, conn):
                self.__server__ = conn.__server__
                self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

            def addUserBinding(self, **kwargs):
                return self.__server__.pem.ad.binding.addUserBinding(kwargs)

            def removeUserBinding(self, **kwargs):
                return self.__server__.pem.ad.binding.removeUserBinding(kwargs)

            def getUserInfo(self, **kwargs):
                return self.__server__.pem.ad.binding.getUserInfo(kwargs)

    def addUser(self, **kwargs):
        return self.__server__.pem.addUser(kwargs)

    def changeUserPassword(self, **kwargs):
        return self.__server__.pem.changeUserPassword(kwargs)

    def disableUser(self, **kwargs):
        return self.__server__.pem.disableUser(kwargs)

    def enableUser(self, **kwargs):
        return self.__server__.pem.enableUser(kwargs)

    def getUserByLogin(self, **kwargs):
        return self.__server__.pem.getUserByLogin(kwargs)

    def getUserInfo(self, **kwargs):
        return self.__server__.pem.getUserInfo(kwargs)

    def getUsers(self, **kwargs):
        return self.__server__.pem.getUsers(kwargs)

    def modifyUser(self, **kwargs):
        return self.__server__.pem.modifyUser(kwargs)

    def removeUser(self, **kwargs):
        return self.__server__.pem.removeUser(kwargs)

    """
    Hosted CRM Management
    """

    @property
    class MSCRM(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def createOrg(self, **kwargs):
            return self.__server__.pem.mscrm.createOrg(kwargs)

        def createUser(self, **kwargs):
            return self.__server__.pem.mscrm.createUser(kwargs)

        def disableOrg(self, **kwargs):
            return self.__server__.pem.mscrm.disableOrg(kwargs)

        def enableOrg(self, **kwargs):
            return self.__server__.pem.mscrm.enableOrg(kwargs)

        def getBusinessUnits(self, **kwargs):
            return self.__server__.pem.mscrm.getBusinessUnits(kwargs)

        def getCurrencies(self, **kwargs):
            return self.__server__.pem.mscrm.getCurrencies(kwargs)

        def getOrgBySubscription(self, **kwargs):
            return self.__server__.pem.mscrm.getOrgBySubscription(kwargs)

        def getOrgInfo(self, **kwargs):
            return self.__server__.pem.mscrm.getOrgInfo(kwargs)

        def getOrgList(self, **kwargs):
            return self.__server__.pem.mscrm.getOrgList(kwargs)

        def getOrgUsers(self, **kwargs):
            return self.__server__.pem.mscrm.getOrgUsers(kwargs)

        def getSecurityRoles(self, **kwargs):
            return self.__server__.pem.mscrm.getSecurityRoles(kwargs)

        def getUserInfo(self, **kwargs):
            return self.__server__.pem.mscrm.getUserInfo(kwargs)

        def modifySecurityRoles(self, **kwargs):
            return self.__server__.pem.mscrm.modifySecurityRoles(kwargs)

        def moveUser(self, **kwargs):
            return self.__server__.pem.mscrm.moveUser(kwargs)

        def removeOrg(self, **kwargs):
            return self.__server__.pem.mscrm.removeOrg(kwargs)

        def removeUser(self, **kwargs):
            return self.__server__.pem.mscrm.removeOrg(kwargs)

        def setExchangeDeliverySettings(self, **kwargs):
            return self.__server__.pem.mscrm.setExchangeDeliverySettings(kwargs)

        def setExternalDeliverySettings(self, **kwargs):
            return self.__server__.pem.mscrm.setExternalDeliverySettings(kwargs)

        def setNoneDeliverySettings(self, **kwargs):
            return self.__server__.pem.mscrm.setNoneDeliverySettings(kwargs)

        def setOrgDisplayName(self, **kwargs):
            return self.__server__.pem.mscrm.setOrgDisplayName(kwargs)

        def setOutlookDeliverySettings(self, **kwargs):
            return self.__server__.pem.mscrm.setOutlookDeliverySettings(kwargs)

        def synchronizeData(self, **kwargs):
            return self.__server__.pem.mscrm.synchronizeData(kwargs)

    """
    Database Management
    """

    def createDatabase(self, **kwargs):
        return self.__server__.pem.createDatabase(kwargs)

    def createDatabaseUser(self, **kwargs):
        return self.__server__.pem.createDatabaseUser(kwargs)

    @property
    class MSSQL(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def setQuota(self, **kwargs):
            return self.__server__.pem.mssql.setQuota(kwargs)

    @property
    class MYSQL(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def applyMySQLActivationParams(self, **kwargs):
            return self.__server__.pem.mysql.applyMySQLActivationParams(kwargs)

    """
    QMail Mailbox Management
    """

    @property
    class CQMAIL(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def addMailbox(self, **kwargs):
            return self.__server__.pem.cqmail.addMailbox(kwargs)

        def addMailForwarding(self, **kwargs):
            return self.__server__.pem.cqmail.addMailForwarding(kwargs)

        def delMailname(self, **kwargs):
            return self.__server__.pem.cqmail.delMailname(kwargs)

        def editMailname(self, **kwargs):
            return self.__server__.pem.cqmail.editMailname(kwargs)

        def editEmailAddresses(self, **kwargs):
            return self.__server__.pem.cqmail.editEmailAddresses(kwargs)

    @property
    class SPAM_ASSASSIN(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def addItems(self, **kwargs):
            return self.__server__.pem.spam_assassin.addItems(kwargs)

        def deleteItems(self, **kwargs):
            return self.__server__.pem.spam_assassin.deleteItems(kwargs)

        def getItems(self, **kwargs):
            return self.__server__.pem.spam_assassin.getItems(kwargs)

    """
    Resource Accounting
    """

    def addResourceType(self, **kwargs):
        return self.__server__.pem.addResourceType(kwargs)

    def addResourceTypeToServiceTemplate(self, **kwargs):
        return self.__server__.pem.addResourceTypeToServiceTemplate(kwargs)

    def getResourceTypesByClass(self, **kwargs):
        return self.__server__.pem.getResourceTypesByClass(kwargs)

    def getResourceUsage(self, **kwargs):
        return self.__server__.pem.getResourceUsage(kwargs)

    def getCustomerSubscriptionsResources(self, **kwargs):
        return self.__server__.pem.getCustomerSubscriptionsResources(kwargs)

    def getResourceUsageForPeriod(self, **kwargs):
        return self.__server__.pem.getResourceUsageForPeriod(kwargs)

    def removeLicense(self, **kwargs):
        return self.__server__.pem.removeLicense(kwargs)

    def resetResourceUsage(self, **kwargs):
        return self.__server__.pem.resetResourceUsage(kwargs)

    def setResourceTypeLimit(self, **kwargs):
        return self.__server__.pem.setResourceTypeLimit(kwargs)

    def setResourceTypeLimits(self, **kwargs):
        return self.__server__.pem.setResourceTypeLimits(kwargs)

    def setRTAttributes(self, **kwargs):
        return self.__server__.pem.setRTAttributes(kwargs)

    @property
    class STATISTICS(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def getStatisticsReport(self, **kwargs):
            return self.__server__.pem.statistics.getStatisticsReport(kwargs)

    def uploadLicense(self, **kwargs):
        return self.__server__.pem.uploadLicense(kwargs)

    """
    Service Template Management
    """

    def activateST(self, **kwargs):
        return self.__server__.pem.activateST(kwargs)

    def addServiceTemplate(self, **kwargs):
        return self.__server__.pem.addServiceTemplate(kwargs)

    def cloneServiceTemplate(self, **kwargs):
        return self.__server__.pem.cloneServiceTemplate(kwargs)

    def deactivateST(self, **kwargs):
        return self.__server__.pem.deactivateST(kwargs)

    def getServiceTemplate(self, **kwargs):
        return self.__server__.pem.getServiceTemplate(kwargs)

    def getServiceTemplateList(self, **kwargs):
        return self.__server__.pem.getServiceTemplateList(kwargs)

    def setSTActivationParams(self, **kwargs):
        return self.__server__.pem.setSTActivationParams(kwargs)

    def setSTRTLimits(self, **kwargs):
        return self.__server__.pem.setSTRTLimits(kwargs)

    """
    Provisioning Attributes Management
    """

    def addProvisioningAttributes(self, **kwargs):
        return self.__server__.pem.addProvisioningAttributes(kwargs)

    def getProvisioningAttributes(self, **kwargs):
        return self.__server__.pem.getProvisioningAttributes(kwargs)

    def setHostAttributes(self, **kwargs):
        return self.__server__.pem.setHostAttributes(kwargs)

    def setHostReadyToProvide(self, **kwargs):
        return self.__server__.pem.setHostReadyToProvide(kwargs)

    def unsetHostAttributes(self, **kwargs):
        return self.__server__.pem.unsetHostAttributes(kwargs)

    """
    IP Pools Management
    """

    def assignIPPool(self, **kwargs):
        return self.__server__.pem.assignIPPool(kwargs)

    def attachIPPool(self, **kwargs):
        return self.__server__.pem.attachIPPool(kwargs)

    def bindIPPool(self, **kwargs):
        return self.__server__.pem.bindIPPool(kwargs)

    def createIPPool(self, **kwargs):
        return self.__server__.pem.createIPPool(kwargs)

    def detachIPPool(self, **kwargs):
        return self.__server__.pem.detachIPPool(kwargs)

    def revokeIPPool(self, **kwargs):
        return self.__server__.pem.revokeIPPool(kwargs)

    def unbindIPPool(self, **kwargs):
        return self.__server__.pem.unbindIPPool(kwargs)

    """
    Native Package Management
    """

    @property
    class PACKAGING(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        @property
        def native_repository(self):
            return self.NATIVE_REPOSITORY

        @property
        class NATIVE_REPOSITORY(object):
            def __init__(self, conn):
                self.__server__ = conn.__server__
                self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

            def createRepository(self, **kwargs):
                return self.__server__.pem.packaging.native_repository.createRepository(kwargs)

            def getRepository(self, **kwargs):
                return self.__server__.pem.packaging.native_repository.getRepository(kwargs)

            def reindex(self, **kwargs):
                return self.__server__.pem.packaging.native_repository.reindex(kwargs)

            def removeRepository(self, **kwargs):
                return self.__server__.pem.packaging.native_repository.removeRepository(kwargs)

    """
    Branding Management
    """

    def brandDomain(self, **kwargs):
        return self.__server__.pem.brandDomain(kwargs)

    def getAvailableSkins(self, **kwargs):
        return self.__server__.pem.getAvailableSkins(kwargs)

    def getBrandInfo(self, **kwargs):
        return self.__server__.pem.getBrandInfo(kwargs)

    def getDomainsForBrandCreation(self, **kwargs):
        return self.__server__.pem.getDomainsForBrandCreation(kwargs)

    def unbrandDomain(self, **kwargs):
        return self.__server__.pem.unbrandDomain(kwargs)

    """
    Hardware Node Management
    """

    def findHost(self, **kwargs):
        return self.__server__.pem.findHost(kwargs)

    def getHost(self, **kwargs):
        return self.__server__.pem.getHost(kwargs)

    def registerSharedNode(self, **kwargs):
        return self.__server__.pem.registerSharedNode(kwargs)

    def registerWindowsNode(self, **kwargs):
        return self.__server__.pem.registerWindowsNode(kwargs)

    """
    Parallels Plesk Panel Management
    """

    def installPleskLicense(self, **kwargs):
        return self.__server__.pem.installPleskLicense(kwargs)

    def revokePleskLicense(self, **kwargs):
        return self.__server__.pem.revokePleskLicense(kwargs)

    """
    Parallels Virtuozzo Containers Management
    """

    @property
    class VZZP(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def attachVPS(self, **kwargs):
            return self.__server__.pem.virtuozzo.attachVPS(kwargs)

        def importTemplate(self, **kwargs):
            return self.__server__.pem.virtuozzo.importTemplate(kwargs)

        def installTemplate(self, **kwargs):
            return self.__server__.pem.virtuozzo.installTemplate(kwargs)

        def installTemplates(self, **kwargs):
            return self.__server__.pem.virtuozzo.installTemplates(kwargs)

        def updateEZTemplates(self, **kwargs):
            return self.__server__.pem.virtuozzo.updateEZTemplates(kwargs)

        def removeTemplates(self, **kwargs):
            return self.__server__.pem.virtuozzo.removeTemplates(kwargs)

        def registerHWNode(self, **kwargs):
            return self.__server__.pem.virtuozzo.registerHWNode(kwargs)

    """
    Global Relay Archiving Management
    """

    @property
    class GLOBAL_RELAY(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def createArchive(self, **kwargs):
            return self.__server__.pem.global_relay.createArchive(kwargs)

        def disableArchive(self, **kwargs):
            return self.__server__.pem.global_relay.disableArchive(kwargs)

        def disableArchiving(self, **kwargs):
            return self.__server__.pem.global_relay.disableArchiving(kwargs)

        def enableArchive(self, **kwargs):
            return self.__server__.pem.global_relay.enableArchive(kwargs)

        def enableArchiving(self, **kwargs):
            return self.__server__.pem.global_relay.enableArchiving(kwargs)

        def getArchive(self, **kwargs):
            return self.__server__.pem.global_relay.getArchive(kwargs)

        def getArchiveRecipients(self, **kwargs):
            return self.__server__.pem.global_relay.getArchiveRecipients(kwargs)

        def getArchiveRecipientsCandidates(self, **kwargs):
            return self.__server__.pem.global_relay.getArchiveRecipientsCandidates(kwargs)

        def retryArchiveOperation(self, **kwargs):
            return self.__server__.pem.global_relay.retryArchiveOperation(kwargs)

    """
    SharePoint Management
    """

    @property
    class SHAREPOINT(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def createSharePointSite(self, **kwargs):
            return self.__server__.pem.sharepoint.createSharePointSite(kwargs)

        def createSharePointSiteInSharedApplication(self, **kwargs):
            return self.__server__.pem.sharepoint.createSharePointSiteInSharedApplication(kwargs)

        def deleteSharePointSite(self, **kwargs):
            return self.__server__.pem.sharepoint.deleteSharePointSite(kwargs)

        def getAvailableSharePointSiteTemplates(self, **kwargs):
            return self.__server__.pem.sharepoint.getAvailableSharePointSiteTemplates(kwargs)

        def addSharePointUser(self, **kwargs):
            return self.__server__.pem.sharepoint.addSharePointUser(kwargs)

        def removeSharePointUser(self, **kwargs):
            return self.__server__.pem.sharepoint.removeSharePointUser(kwargs)

        def modifySharePointSiteLimits(self, **kwargs):
            return self.__server__.pem.sharepoint.modifySharePointSiteLimits(kwargs)

    @property
    class AM(object):

        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def setAccountCCPVersion(self, **kwargs):
            return self.__server__.am.setAccountCCPVersion(kwargs)

    """
    Exchange Management
    """

    @property
    class EXCHANGE(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def addMailbox(self, **kwargs):
            return self.__server__.pem.exchange.addMailbox(kwargs)

        def disableForwarding(self, **kwargs):
            return self.__server__.pem.exchange.disableForwarding(kwargs)

        def enableForwarding(self, **kwargs):
            return self.__server__.pem.exchange.enableForwarding(kwargs)

        def getEmailAddresses(self, **kwargs):
            return self.__server__.pem.exchange.getEmailAddresses(kwargs)

        def getMailboxByEmailAddress(self, **kwargs):
            return self.__server__.pem.exchange.getMailboxByEmailAddress(kwargs)

        def getMailboxes(self, **kwargs):
            return self.__server__.pem.exchange.getMailboxes(kwargs)

        def getMailboxInfo(self, **kwargs):
            return self.__server__.pem.exchange.getMailboxInfo(kwargs)

        def getMailboxStores(self, **kwargs):
            return self.__server__.pem.exchange.getMailboxStores(kwargs)

        def getUserMailbox(self, **kwargs):
            return self.__server__.pem.exchange.getUserMailbox(kwargs)

        def modifyMailbox(self, **kwargs):
            return self.__server__.pem.exchange.modifyMailbox(kwargs)

        def moveMailboxes(self, **kwargs):
            return self.__server__.pem.exchange.moveMailboxes(kwargs)

        def removeMailbox(self, **kwargs):
            return self.__server__.pem.exchange.removeMailbox(kwargs)

        def addBlackBerry(self, **kwargs):
            return self.__server__.pem.exchange.addBlackBerry(kwargs)

        def getBlackBerryInfo(self, **kwargs):
            return self.__server__.pem.exchange.getBlackBerryInfo(kwargs)

        def getSubscriptionBlackBerryInfo(self, **kwargs):
            return self.__server__.pem.exchange.getSubscriptionBlackBerryInfo(kwargs)

        def removeBlackBerry(self, **kwargs):
            return self.__server__.pem.exchange.removeBlackBerry(kwargs)

        def setBlackBerryActivationPassword(self, **kwargs):
            return self.__server__.pem.exchange.setBlackBerryActivationPassword(kwargs)

        def setBlackBerryITPolicy(self, **kwargs):
            return self.__server__.pem.exchange.setBlackBerryITPolicy(kwargs)

        def wipeBlackBerry(self, **kwargs):
            return self.__server__.pem.exchange.wipeBlackBerry(kwargs)

        def addGoodlink(self, **kwargs):
            return self.__server__.pem.exchange.addGoodlink(kwargs)

        def addMailboxWithTemplate(self, **kwargs):
            return self.__server__.pem.exchange.addMailboxWithTemplate(kwargs)

        def changeMailboxTemplate(self, **kwargs):
            return self.__server__.pem.exchange.changeMailboxTemplate(kwargs)

        def getMailboxTemplates(self, **kwargs):
            return self.__server__.pem.exchange.getMailboxTemplates(kwargs)

        def forceMailboxTemplatesUsing(self, **kwargs):
            return self.__server__.pem.exchange.forceMailboxTemplatesUsing(kwargs)

        def getOutlookLicense(self, **kwargs):
            return self.__server__.pem.exchange.getOutlookLicense(kwargs)

        def disableOutlookLicense(self, **kwargs):
            return self.__server__.pem.exchange.disableOutlookLicense(kwargs)

        def enableOutlookLicense(self, **kwargs):
            return self.__server__.pem.exchange.enableOutlookLicense(kwargs)

        def assignMasterAccount(self, **kwargs):
            return self.__server__.pem.exchange.assignMasterAccount(kwargs)

        def unassignMasterAccount(self, **kwargs):
            return self.__server__.pem.exchange.unassignMasterAccount(kwargs)

        def getMasterAccountInfo(self, **kwargs):
            return self.__server__.pem.exchange.getMasterAccountInfo(kwargs)

        def enableSPLAFeature(self, **kwargs):
            return self.__server__.pem.exchange.enableSPLAFeature(kwargs)

        def disableSPLAFeature(self, **kwargs):
            return self.__server__.pem.exchange.disableSPLAFeature(kwargs)

        def addDistributionList(self, **kwargs):
            return self.__server__.pem.exchange.addDistributionList(kwargs)

        def addDistributionListMembers(self, **kwargs):
            return self.__server__.pem.exchange.addDistributionListMembers(kwargs)

        def getDistributionList(self, **kwargs):
            return self.__server__.pem.exchange.getDistributionList(kwargs)

        def getDistributionLists(self, **kwargs):
            return self.__server__.pem.exchange.getDistributionLists(kwargs)

        def modifyDistributionList(self, **kwargs):
            return self.__server__.pem.exchange.modifyDistributionList(kwargs)

        def removeDistributionListMembers(self, **kwargs):
            return self.__server__.pem.exchange.removeDistributionListMembers(kwargs)

        def removeDistributionList(self, **kwargs):
            return self.__server__.pem.exchange.removeDistributionList(kwargs)

        def addPublicFolder(self, **kwargs):
            return self.__server__.pem.exchange.addPublicFolder(kwargs)

        def mailEnablePublicFolder(self, **kwargs):
            return self.__server__.pem.exchange.mailEnablePublicFolder(kwargs)

        def mailDisablePublicFolder(self, **kwargs):
            return self.__server__.pem.exchange.mailDisablePublicFolder(kwargs)

        def getRootFolderName(self, **kwargs):
            return self.__server__.pem.exchange.getRootFolderName(kwargs)

        def getPublicFolders(self, **kwargs):
            return self.__server__.pem.exchange.getPublicFolders(kwargs)

        def removePublicFolder(self, **kwargs):
            return self.__server__.pem.exchange.removePublicFolder(kwargs)

        def grantPublicFolderRoles(self, **kwargs):
            return self.__server__.pem.exchange.grantPublicFolderRoles(kwargs)

        def revokePublicFolderRoles(self, **kwargs):
            return self.__server__.pem.exchange.revokePublicFolderRoles(kwargs)

        def listPublicFolderRoles(self, **kwargs):
            return self.__server__.pem.exchange.listPublicFolderRoles(kwargs)

        def addContact(self, **kwargs):
            return self.__server__.pem.exchange.addContact(kwargs)

        def getContact(self, **kwargs):
            return self.__server__.pem.exchange.getContact(kwargs)

        def getContacts(self, **kwargs):
            return self.__server__.pem.exchange.getContacts(kwargs)

        def modifyContact(self, **kwargs):
            return self.__server__.pem.exchange.modifyContact(kwargs)

        def removeContact(self, **kwargs):
            return self.__server__.pem.exchange.removeContact(kwargs)

        def addResourceMailbox(self, **kwargs):
            return self.__server__.pem.exchange.addResourceMailbox(kwargs)

        def getResourceMailboxes(self, **kwargs):
            return self.__server__.pem.exchange.getResourceMailboxes(kwargs)

        def modifyResourceMailbox(self, **kwargs):
            return self.__server__.pem.exchange.modifyResourceMailbox(kwargs)

        def getDeliveryPermissions(self, **kwargs):
            return self.__server__.pem.exchange.getDeliveryPermissions(kwargs)

        def getDeliveryPermissionsCandidates(self, **kwargs):
            return self.__server__.pem.exchange.getDeliveryPermissionsCandidates(kwargs)

        def grantDeliveryPermissions(self, **kwargs):
            return self.__server__.pem.exchange.grantDeliveryPermissions(kwargs)

        def revokeDeliveryPermissions(self, **kwargs):
            return self.__server__.pem.exchange.revokeDeliveryPermissions(kwargs)

        def getMailboxPermissions(self, **kwargs):
            return self.__server__.pem.exchange.getMailboxPermissions(kwargs)

        def getMailboxPermissionsCandidates(self, **kwargs):
            return self.__server__.pem.exchange.getMailboxPermissionsCandidates(kwargs)

        def grantMailboxPermissions(self, **kwargs):
            return self.__server__.pem.exchange.grantMailboxPermissions(kwargs)

        def revokeMailboxPermissions(self, **kwargs):
            return self.__server__.pem.exchange.revokeMailboxPermissions(kwargs)

        def enableUnifiedMessaging(self, **kwargs):
            return self.__server__.pem.exchange.enableUnifiedMessaging(kwargs)

        def disableUnifiedMessaging(self, **kwargs):
            return self.__server__.pem.exchange.disableUnifiedMessaging(kwargs)

        def addEmailAddresses(self, **kwargs):
            return self.__server__.pem.exchange.addEmailAddresses(kwargs)

        def changePrimaryEmailAddress(self, **kwargs):
            return self.__server__.pem.exchange.changePrimaryEmailAddress(kwargs)

        def getEmailDomains(self, **kwargs):
            return self.__server__.pem.exchange.getEmailDomains(kwargs)

        def getSMTPFilters(self, **kwargs):
            return self.__server__.pem.exchange.getSMTPFilters(kwargs)

        def removeEmailAddresses(self, **kwargs):
            return self.__server__.pem.exchange.removeEmailAddresses(kwargs)

    """
    Application Management
    """

    @property
    class aps(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def getApplicationInstances(self, **kwargs):
            return self.__server__.pem.APS.getApplicationInstances(kwargs)

        def getApplicationInstance(self, **kwargs):
            return self.__server__.pem.APS.getApplicationInstance(kwargs)

        def getApplicationInstanceSettings(self, **kwargs):
            return self.__server__.pem.APS.getApplicationInstanceSettings(kwargs)

        def getApplicationByPackage(self, **kwargs):
            return self.__server__.pem.APS.getApplicationByPackage(kwargs)

        def getApplicationToken(self, **kwargs):
            return self.__server__.pem.APS.getApplicationToken(kwargs)

        def getAccountToken(self, **kwargs):
            return self.__server__.pem.APS.getAccountToken(kwargs)

        def getUserToken(self, **kwargs):
            return self.__server__.pem.APS.getUserToken(kwargs)

        def getApplicationSettings(self, **kwargs):
            return self.__server__.pem.APS.getApplicationSettings(kwargs)

        def getPackage(self, **kwargs):
            return self.__server__.pem.APS.getPackage(kwargs)

        def getProvisioningSettings(self, **kwargs):
            return self.__server__.pem.APS.getProvisioningSettings(kwargs)

        def getSubscriptionApplicationInstances(self, **kwargs):
            return self.__server__.pem.APS.getSubscriptionApplicationInstances(kwargs)

        def importPackage(self, **kwargs):
            return self.__server__.pem.APS.importPackage(kwargs)

        def provideApplicationInstance(self, **kwargs):
            return self.__server__.pem.APS.provideApplicationInstance(kwargs)

        def removeApplication(self, **kwargs):
            return self.__server__.pem.APS.removeApplication(kwargs)

        def setApplicationInstanceSettings(self, **kwargs):
            return self.__server__.pem.APS.setApplicationInstanceSettings(kwargs)

        def unimportPackage(self, **kwargs):
            return self.__server__.pem.APS.unimportPackage(kwargs)

        def unprovideApplicationInstance(self, **kwargs):
            return self.__server__.pem.APS.unprovideApplicationInstance(kwargs)

        def upgradeApplicationInstance(self, **kwargs):
            return self.__server__.pem.APS.upgradeApplicationInstance(kwargs)

        def getApplicationLicenseInfo(self, **kwargs):
            return self.__server__.pem.APS.getApplicationLicenseInfo(kwargs)

        def getApplicationInstanceLicenseActivationData(self, **kwargs):
            return self.__server__.pem.APS.getApplicationInstanceLicenseActivationData(kwargs)

        def installApplicationInstanceLicense(self, **kwargs):
            return self.__server__.pem.APS.installApplicationInstanceLicense(kwargs)

        def removeApplicationInstanceLicense(self, **kwargs):
            return self.__server__.pem.APS.removeApplicationInstanceLicense(kwargs)

        def registerUserInApplicationInstance(self, **kwargs):
            return self.__server__.pem.APS.registerUserInApplicationInstance(kwargs)

        def getServiceInstances(self, **kwargs):
            return self.__server__.pem.APS.getServiceInstances(kwargs)

        def setServiceInstanceResourceType(self, **kwargs):
            return self.__server__.pem.APS.setServiceInstanceResourceType(kwargs)

        def provideServiceInstance(self, **kwargs):
            return self.__server__.pem.APS.provideServiceInstance(kwargs)

        def unprovideServiceInstance(self, **kwargs):
            return self.__server__.pem.APS.unprovideServiceInstance(kwargs)

        def setServiceInstanceSettings(self, **kwargs):
            return self.__server__.pem.APS.setServiceInstanceSettings(kwargs)

        def getApplicationInstanceServiceResourceTypes(self, **kwargs):
            return self.__server__.pem.APS.getApplicationInstanceServiceResourceTypes(kwargs)

        def getApplications(self, **kwargs):
            return self.__server__.pem.APS.getApplications(kwargs)

        def getUserServiceInstances(self, **kwargs):
            return self.__server__.pem.APS.getUserServiceInstances(kwargs)

    """
    External System Management
    """

    def getExternalSystemList(self, **kwargs):
        return self.__server__.pem.getExternalSystemList(kwargs)

    def registerExternalSystem(self, **kwargs):
        return self.__server__.pem.registerExternalSystem(kwargs)

    def setExternalSystemConfig(self, **kwargs):
        return self.__server__.pem.setExternalSystemConfig(kwargs)

    def unregisterExternalSystem(self, **kwargs):
        return self.__server__.pem.unregisterExternalSystem(kwargs)

    """
    Transactional Extension
    """

    def batchRequest(self, **kwargs):
        return self.__server__.pem.batchRequest(kwargs)

    def getRequestStatus(self, **kwargs):
        return self.__server__.pem.getRequestStatus(kwargs)

    @property
    class TXN(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def Begin(self, **kwargs):
            return self.__server__.txn.Begin(kwargs)

        def Commit(self, **kwargs):
            return self.__server__.txn.Commit(kwargs)

        def Rollback(self, **kwargs):
            return self.__server__.txn.Rollback(kwargs)

    @property
    class TASKS(object):
        def __init__(self, conn):
            self.__server__ = conn.__server__
            self.__server__._ServerProxy__verbose = conn.__server__._ServerProxy__verbose

        def rescheduleTask(self, **kwargs):
            return self.__server__.pem.tasks.rescheduleTask(kwargs)

    def create_account(self, first_name=None, last_name=None, account_type='C',
                       branded_domain=None, parent_account_id=None, **kwargs):
        """
        Possible values for the account_type:
            'C': Indicates that the Account is created for Customer. Default value.
            'R': Indicates that the Account is created for Reseller.
        If company param is present in call, this one is bypassed to openapi call, this one
        is optional parameter in call and causes different behaivour on how account is called
        (personal vs business)
        If first_name, last_name are different than none, autogeneration is user_id
        if email param is present in input, is used, otherwise is random generated
        """
        if not first_name:
            first_name = rand_id(10)

        if not last_name:
            last_name = rand_id(10)

        if 'company' in kwargs:
            company_name = kwargs['company']
            person = {
                'first_name': first_name,
                'last_name': last_name,
                'company_name': company_name}
        else:
            person = {'first_name': first_name, 'last_name': last_name}

        address = {'street_name': rand_id(10), 'zipcode': rand_id(
            10, string.digits), 'city': rand_id(10), 'country': 'ru', 'state': rand_id(10)}
        phone = {'country_code': rand_id(3, string.digits), 'area_code': rand_id(
            4, string.digits), 'phone_num': rand_id(10, string.digits), 'ext_num': ''}

        data = {
            'account_type': account_type,
            'person': person,
            'address': kwargs.get('address', address),
            'phone': kwargs.get('phone', phone),
            'email': kwargs.get('email', '%s@%s.com' % (rand_id(10), rand_id(8)))
        }

        if branded_domain:
            data['branded_domain'] = branded_domain

        if parent_account_id:
            data['parent_account_id'] = parent_account_id

        return self.addAccount(**data)

    def create_account_member(self, account_id, login, password='password', **kwargs):
        first_name = kwargs.get('first_name', rand_id(10))
        last_name = kwargs.get('last_name', rand_id(10))
        email = kwargs.get('email', '%s@%s.com' % (rand_id(10), rand_id(8)))

        # Forcing difference between user_id and member_id as happened in #APS-19910
        # Note: if we ever face an error like "user_id already exists - need to add retry here
        _user_id = random.randint(2 ** 20, 2 ** 31 - 1)

        address = {
            'street_name': rand_id(10),
            'zipcode': rand_id(10, string.digits),
            'city': rand_id(10),
            'country': 'ru',
            'state': rand_id(10)
        }
        phone = {
            'country_code': rand_id(3, string.digits),
            'area_code': rand_id(4, string.digits),
            'phone_num': rand_id(10, string.digits),
            'ext_num': ''
        }

        member = self.addAccountMember(
            account_id=account_id,
            user_id=_user_id,
            auth={'login': login, 'password': password},
            person={'first_name': first_name, 'last_name': last_name},
            address=kwargs.get('address', address),
            phone=kwargs.get('phone', phone),
            email=email
        )

        # !ATTENTION!
        # user_id returned from the pem.addAccountMember call is not actualy user_id, but member_id
        # and needs to be translated to the real user_id via pem.getMemberFullInfo call
        # !ATTENTION!

        # If you need to convert member_id to user_id, you need to use the following code
        # member_info = self.pem.getMemberFullInfo( member_id = member['user_id'] )
        # user_id = member_info['user_id']

        return member


class Transaction:
    def __init__(self, api, wait=True, timeout=2400):
        self.api = api
        self._wait = wait
        self.timeout = timeout

    def __enter__(self):
        self.request_id, self.txn_id = self.api.TXN.Begin()
        self.api.txn_id = self.txn_id
        return self.api

    def __exit__(self, type, value, tb):
        self.api.TXN.Commit(txn_id=self.txn_id)

        if self._wait:
            self.wait(self.request_id)

    def wait(self, task_id):
        # sleep 1 second to let API-getters to finish
        time.sleep(1)
        r = self.api.getRequestStatus(request_id=task_id)
        if r['status'] == -1:
            raise Exception(r['error_message'])
        status = r['result']
        wait_time = 0
        i = 1
        while status['request_status'] == 1:
            time.sleep(5 * i)
            wait_time += 5 * i
            status = self.api.getRequestStatus(request_id=task_id)['result']
            if wait_time >= self.timeout:
                raise Exception("Operation timeout=%s is reached." % self.timeout)
            if status['request_status'] == 0:
                return True
            elif status['request_status'] == 2:
                raise Exception("Operation failed. %s" % status['status_messages'])
            if i < 6:
                i += 1
