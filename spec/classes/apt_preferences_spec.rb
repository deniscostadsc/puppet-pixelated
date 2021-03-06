require 'spec_helper'

describe 'pixelated::apt::preferences' do
  let(:facts) do
      {
        :operatingsystem => 'Debian',
        :lsbdistid       => 'Debian',
        :lsbdistcodename => 'wheezy',
      }
  end
  it { should contain_file('/etc/apt/preferences.d/python-tornado').with_content(/Pin: release o=pixelated/) }
  it { should contain_file('/etc/apt/preferences.d/soledad-server').with_content(/Pin: release o=pixelated/) }
  it { should contain_file('/etc/apt/preferences.d/soledad-common').with_content(/Pin: release o=pixelated/) }
  it { should contain_file('/etc/apt/preferences.d/soledad-client').with_content(/Pin: release o=pixelated/) }
  it { should contain_file('/etc/apt/preferences.d/leap-keymanager').with_content(/Pin: release o=pixelated/) }
  it { should contain_file('/etc/apt/preferences.d/leap-auth').with_content(/Pin: release o=pixelated/) }
  it { should contain_file('/etc/apt/preferences.d/python-tornado').with_content(/Package: python-tornado/) }
  it { should contain_file('/etc/apt/preferences.d/python-tornado').with_content(/Pin-Priority: 999/) }

  %w( python-urllib3 python-requests python-six linux-image-amd64).each do | package |
    it { should contain_file("/etc/apt/preferences.d/#{package}").with_content(/wheezy/) }
  end

end
